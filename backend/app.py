from fastapi import FastAPI
import pickle
import os
from pydantic import BaseModel
from backend.src.text_utils import transform_text


BASE_DIR = os.path.abspath(os.path.dirname(__file__)) 
MODEL_PATH = os.path.join(BASE_DIR, "model", "Model.pkl")
VEC_PATH = os.path.join(BASE_DIR, "model", "vectorizer.pkl")

app=FastAPI()

class Message(BaseModel):
    message: str

model = pickle.load(open(MODEL_PATH, "rb"))
vectorizer = pickle.load(open(VEC_PATH, "rb"))

@app.post("/predict")
def predict(msg:Message):
    clean_text = transform_text(msg.message)
    X = vectorizer.transform([clean_text])

    result=model.predict(X)[0]
    return {"prediction":int(result)}

