

# 🛡️ AI Foul Language Detection System

## 🚀 Overview

This project is an AI-based content moderation system that detects foul or abusive language in user-generated text.

It supports:
- **English foul detection** using a pretrained transformer-based sentiment analysis model (no hardcoded list).
- **Hindi foul detection (written in Roman script)** using fuzzy matching on commonly used abusive terms.

The system is designed to handle inputs in either language and flag them as clean or inappropriate based on context and content.

---

## 🎯 Problem Statement

> Build a foul language detection system that does not rely on a static list of abusive words in English, and also handles detection in one Indian language (e.g., Hindi written in Roman script).

---

## 🧠 Approach

### ✅ English Detection (Level 1 - AI-based)
- We use a **pretrained transformer model**:  
  `distilbert-base-uncased-finetuned-sst-2-english` from HuggingFace.
- This model classifies text as **POSITIVE** or **NEGATIVE**, and we treat high-confidence *negative* results as foul.

### ✅ Hindi Detection (Level 2 - Fuzzy Logic)
- Hindi abuses in Roman script (like `"bkl"`, `"randi"`, `"chutiya"`) are hard to detect via AI sentiment models.
- We handle these using **fuzzy string matching** against a curated list of common Hindi slurs (no need for native script or translation).
- Even typos or slang-like variations (e.g., `"chutya"`, `"bkl"`) are detected.

---

## 🖥️ How It Works

- User inputs text (e.g., a comment or post).
- The app analyzes it using:
  1. **AI sentiment model** for English
  2. **Fuzzy logic** for Hindi
- It then flags the text as:
  - ✅ Clean
  - ❌ Foul (in English or Hindi)

---

## 🌟 Example Inputs

| Input                          | Detected As      |
|--------------------------------|------------------|
| "What a beautiful day!"        | ✅ Clean          |
| "You're such a moron!"         | ❌ English foul   |
| "Tu ek bkl hai"                | ❌ Hindi foul     |
| "randi"                        | ❌ Hindi foul     |
| "Good morning, hope you're well!" | ✅ Clean       |

> Note: The sentiment model may misclassify Roman Hindi slurs (like "randi") as POSITIVE due to vocabulary limitations. Our Level 2 detection compensates for this.

---

## 💻 Tech Stack

- [Transformers – HuggingFace](https://huggingface.co/)
- PyTorch
- FuzzyWuzzy (string matching)
- Streamlit (UI)

---

## 🔧 Run the Project Locally

```bash
# 1. (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 2. Install required packages
pip install -r requirements.txt

# 3. Launch the app
streamlit run app.py
