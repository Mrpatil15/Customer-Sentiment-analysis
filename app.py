import streamlit as st
import pickle
from utils import preprocess_text

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Streamlit UI
st.title("Customer Review Sentiment Analysis")
st.write("Classifies a review as Positive, Neutral, or Negative.")

user_input = st.text_area("Enter your review here:")

if st.button("Analyze Sentiment"):
    if user_input.strip():
        processed = preprocess_text(user_input)
        transformed = vectorizer.transform([processed])
        prediction = model.predict(transformed)[0]
        st.markdown(f"### Sentiment: {prediction}")
    else:
        st.warning("Please enter a review.") 