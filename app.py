import streamlit as st
import pickle

# Load saved model and vectorizer
model = pickle.load(open("fake_news_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# UI Title
st.title("📰 Fake News Detection App")
st.write("Enter news text below to check if it is REAL or FAKE")

# Text input
news_input = st.text_area("Enter News Content")

# Predict button
if st.button("Check News"):
    if news_input.strip() != "":
        # Transform input
        vector_input = vectorizer.transform([news_input])
        
        # Prediction
        prediction = model.predict(vector_input)
        
        # Output
        if prediction[0] == "fake":
            st.error("⚠️ This news is FAKE")
        else:
            st.success("✅ This news is REAL")
    else:
        st.warning("Please enter some text")