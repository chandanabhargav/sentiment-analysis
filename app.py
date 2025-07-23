import streamlit as st
from transformers import pipeline

# Load model
st.title("Sentiment Classifier")
st.markdown("Enter a sentence to detect whether it's **Positive** or **Negative**.")

classifier = pipeline("sentiment-analysis")

# Input
text = st.text_area("✍️ Enter your sentence:", height=150)

# Predict
if st.button("Predict Sentiment"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        result = classifier(text[:512])[0]
        st.success(f"**Label:** {result['label']}")
        st.info(f"**Confidence:** {round(result['score'], 3)}")
