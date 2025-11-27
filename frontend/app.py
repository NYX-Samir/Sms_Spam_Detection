import streamlit as st
import requests

API_URL="http://127.0.0.1:8000/predict"

st.title("SMS SPAM DETECTION")
input_sms=st.text_area("Enter your message")

if st.button("Predict"):
    payload={"message":input_sms}
    response=requests.post(API_URL,json=payload)
    
    if response.status_code==200:
        result=response.json().get("prediction",0)
        st.write("Spam" if result==1 else "Ham")
        
    else:
        st.write("Error:API not responding")
        



