# Fake News Detection: A Rule-Based NLP Pipeline

## Project Overview

This project implements a custom-built fake news detection pipeline, crafted entirely without pre-trained NLP libraries. It explores the raw art of language processing using regular expressions, rule-based heuristics, and hand-engineered features. Our goal was not just to detect fake news—but to **understand** the language beneath.

---

##  Dataset

The data consists of two sets of text documents:
- `real_news.csv` — collection of verified, factual headlines/articles.
- `fake_news.csv` — curated headlines/articles identified as misinformation or hoaxes.

Each document is labeled as either `REAL`(=1) or `FAKE`(=0).

---

## Custom Components

### 1. **Tokenizer**
- **Handles informal language**, contractions (`he’s → he is / he has`), punctuation, emoticons (`:)`etc.), and casing.
- **Repeated Character Normalization**: Converts elongated words (`sooooo → so <REPEAT:5>`).
- **Emoji & Symbol Extraction** using regular expressions.
- **Contraction Expansion**: A hand-defined map for common English contractions.

### 2. **POS Tagger (Rule-Based)**
- Tags tokens using regex and suffix rules.
- Coarse POS categories: `noun`, `verb`, `adjective`, `adverb`, `determiner`, etc.
- Uses suffix cues like `-ing`, `-ed`, `-ly`, etc. to infer parts of speech.
- Ignores special tokens like `<REPEAT:n>` during tagging.

### 3. **Lemmatizer**
- Reduces inflected forms to base forms using custom POS-aware rules:
  - `running → run` (if POS is `verb`)
  - `protagonists → protagonist` (if POS is `noun`)
- Handles edge cases like double consonants (`runn` → `run`) after stripping.

---

## Feature Engineering

### 1. **Bag-of-Words (BoW)**
- Built from scratch using term frequencies.
- Supports minimum frequency filtering.
- This isn't used in pipeline though
### 2. **TF-IDF**
- Implemented from the ground up.
- Calculates:
  - **TF**: Token frequency in a document.
  - **IDF**: Inverse Document Frequency across corpus.
- Final vector: `TF × IDF`.

---

## Model Training

Two classifiers were trained and compared:
- **Naïve Bayes (Multinomial)**
- **Support Vector Machine (SVM)**

Each was trained on:
- BOW vectors
- TF-IDF vectors

---

##  Evaluation

| Metric      | Naïve Bayes | SVM     |
|-------------|-------------|---------|
| Accuracy    | `0.9637`    |`0.9964` |
| F1 Score    | `0.9637`    | `0.9964` |


###  Additional Visualizations
- Token frequency histograms
- `<REPEAT:n>` token distribution(I initially eliminated these)
- Confusion matrices
- ROC curves
- Word clouds (optional)

---

## Notes

- All text was lemmatized using **custom logic**, guided by our POS tagger.
- The tokenizer plays a **central role** in enabling the rule-based pipeline.
- No spaCy, NLTK, or transformers were used—this is **from scratch**.
- Emphasis on **explainability and interpretability** over raw accuracy.

---

## 📂 Folder Structure


