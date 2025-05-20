import json
import re
from typing import List
#function to convert 2 lines of json data to 1 line
def fix_multiline_jsonl(input_path, output_path):
    fixed_count = 0
    error_count = 0
    buffer = ""
    with open(input_path, "r", encoding="utf-8") as infile, open(output_path, "w", encoding="utf-8") as outfile:
        for line in infile:
            line = line.strip()
            if not line:#skip the empty lines
                continue

            buffer += line + " "

            try:
                #try to parse the current buffer
                obj = json.loads(buffer)
                outfile.write(json.dumps(obj) + "\n")
                fixed_count += 1
                buffer = ""  #clear buffer after success
            except json.JSONDecodeError:
                continue  

        if buffer:
            try:
                obj = json.loads(buffer)
                outfile.write(json.dumps(obj) + "\n")
                fixed_count += 1
            except json.JSONDecodeError as e:
                print(f"⚠️ Final leftover block failed: {e}")
                error_count += 1

    print(f"✅ Fixed: {fixed_count} entries written to {output_path}")
    if error_count:
        print(f"❌ {error_count} entries could not be fixed.")

#call the function
fix_multiline_jsonl("/content/tool invocation.json", "/content/corrected.json")
