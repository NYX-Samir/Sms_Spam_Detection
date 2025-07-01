import streamlit as st
import pickle
from text_utils import transform_text

import nltk
nltk.download('punkt')
nltk.download('stopwords')

# load vectorizer and model
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('Model.pkl', 'rb'))

st.title("SMS SPAM Detector")

input_sms = st.text_area("Enter the message")

if st.button('Check'):
    # preprocess
    transformed_sms = transform_text(input_sms)
    # vectorize
    vector_input = tfidf.transform([transformed_sms]).toarray()
    # predict
    result = model.predict(vector_input)[0]
    # display
    if result == 1:
        st.header("It’s a Spam ❌")
    else:
        st.header("It’s not a Spam ✅")
