import streamlit as st
from detector import analyze_text, english_classifier

st.set_page_config(page_title="AI Foul Language Detector", layout="centered")

# ---------------- Title and Description ----------------
st.title("🛡️ AI Foul Language Detection System")
st.markdown("""
This app detects foul language in:
- **English**, using a pretrained AI model for sentiment classification
- **Hindi (Roman script)**, using fuzzy matching on common offensive words

No hardcoded list is used for English – this is an AI-powered approach.
""")

st.markdown("---")

# ---------------- Input Section ----------------
st.subheader("📩 Enter Text to Analyze")
user_input = st.text_area("Write your content here:", height=150)

# ---------------- Example Buttons ----------------
with st.expander("💡 See Example Inputs"):
    st.markdown("""
    - ✅ `"What a wonderful day!"`  
    - ❌ (English foul) `"You're such a moron!"`  
    - ❌ (Hindi foul) `"Tu ek bkl hai"`

    Try changing them and observing results below.
    """)

# ---------------- Submit Button ----------------
if st.button("🔍 Scan for Foul Language"):
    if not user_input.strip():
        st.warning("⚠️ Please enter some content to scan.")
    else:
        result = analyze_text(user_input)

        # Sentiment confidence (optional)
        sentiment = english_classifier(user_input)[0]
        score = round(sentiment['score'] * 100, 2)
        label = sentiment['label']

        st.markdown("---")
        if "✅" in result:
            st.success(result)
            st.markdown(f"**Sentiment:** {label} ({score}%)")
        else:
            st.error(result)
            st.markdown(f"**Sentiment:** {label} ({score}%)")

        st.markdown("---")

# ---------------- Footer ----------------
st.markdown(
    """
    <hr style="margin-top: 40px;">
    <p style="text-align: center; font-size: 14px;">
    Created by <b>Vaibhav Saini</b> | AI/ML | IIT BHU | 2026
    </p>
    """, unsafe_allow_html=True
)
