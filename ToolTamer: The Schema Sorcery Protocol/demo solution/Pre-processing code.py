def clean_schema(system_str: str) -> str:
    """extract JSON object from messy system prompt"""
    match = re.search(r'{.*}', system_str, re.DOTALL)
    if not match:
        return ""
    #this step is for debugging
    try:
        schema_json = json.loads(match.group(0))
        return json.dumps([schema_json], sort_keys=True)
    except json.JSONDecodeError as e:
        print("Schema parse error:", e)
        return ""

def extraction(assistant_str:str):
  match=re.search(r'<functioncall>\s*(\{.*?\})\s*<\|endoftext\|>',assistant_str,re.DOTALL)
  if not match:
    print("no functional call block found")
    return None
  #this step is for debugging
  try:
    fn_call=json.loads(match.group(1))
    return json.dumps(fn_call,sort_keys=True)
  except json.JSONDecodeError:
    print("Assistant functioncall parse failed:", e)
    return None

def parse_chat_log(chat_str: str) -> List[dict]:
    """extract user turns and assistant responses/tool calls"""
    samples = []
    # Find all user messages
    user_turns = re.findall(r'USER:(.*?)ASSISTANT:', chat_str, re.DOTALL)
    # Find all assistant messages (can include tool calls)
    assistant_turns = re.findall(r'ASSISTANT:(.*?)(USER:|<\|endoftext\|>|$)', chat_str, re.DOTALL)
    return [(u.strip(), a[0].strip()) for u, a in zip(user_turns, assistant_turns)]

def preprocess_custom_chat(entry):
    schema_str = clean_schema(entry.get("system", ""))
    if not schema_str:
        return []
    parsed_pairs = parse_chat_log(entry.get("chat", ""))
    samples = []
    for user, assistant in parsed_pairs:
        sample = {"input": f"<system>{schema_str}</system>\n<user>{user}</user>"}
        if "<functioncall>" in assistant:
            fn_json = extraction(assistant)
            if fn_json:
                sample["output"] = fn_json
            else:
                continue  #skip malfunctioning tool calls
        else:
            sample["output"] = assistant
        samples.append(sample)
    return samples
#if __name__ == "__main__":
#to avoid the hugeness of the tool invocation.json file a smaller sample is used here
with open("/content/sample01.json", "r") as f:
    for line_num, line in enumerate(f): # Added enumerate to get line number
        try:
            entry = json.loads(line)
        except json.JSONDecodeError as e:
            print(f"[SKIP] Line {line_num + 1} not valid JSON: {e}") # Added line number for better debugging
            continue # Skip to the next line if JSON decoding fails
        processed = preprocess_custom_chat(entry)
      """you can use next 3 lines to see the results"""
        #print("final Output:")
        # for item in processed:
        #     print(json.dumps(item, indent=2))
