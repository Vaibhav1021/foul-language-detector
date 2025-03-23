from transformers import pipeline
from fuzzywuzzy import fuzz

# Use sentiment-analysis model safely (fully compatible with Streamlit on Windows)
english_classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Hindi Roman word list
hindi_foul_words = [
    "chutiya", "madarchod", "bhenchod", "gandu", "bhosdike",
    "bkl", "mc", "bc", "gaand", "lund", "chod", "randi"
]

def is_english_foul(text, threshold=0.8):
    result = english_classifier(text)[0]
    if result['label'] == 'NEGATIVE' and result['score'] > threshold:
        return True
    return False

def is_hindi_foul(text, fuzz_threshold=85):
    words = text.lower().split()
    for word in words:
        for foul in hindi_foul_words:
            if fuzz.partial_ratio(word, foul) >= fuzz_threshold:
                return True
    return False

def analyze_text(text):
    level_1 = is_english_foul(text)
    level_2 = is_hindi_foul(text)

    if level_1:
        return "❌ Rejected: Foul language detected in English (Level 1)"
    elif level_2:
        return "❌ Rejected: Foul language detected in Hindi (Level 2)"
    else:
        return "✅ Clean: Content is acceptable"

# Export classifier to access in Streamlit app
__all__ = ["analyze_text", "english_classifier"]
