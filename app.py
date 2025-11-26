import streamlit as st
import pickle
from src.text_utils import transform_text

model = pickle.load(open(r"model\Model.pkl", "rb"))
vectorizer = pickle.load(open(r"model\vectorizer.pkl", "rb"))

st.title("SMS Spam Detector")
input_sms = st.text_area("Enter your message")

if st.button("Predict"):
    vectorized = vectorizer.transform([input_sms])
    result = model.predict(vectorized)[0]
    st.write("Spam" if result == 1 else "Ham")

