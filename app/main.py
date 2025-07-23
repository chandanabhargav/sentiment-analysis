from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

classifier = pipeline('sentiment-analysis')

class TextInput(BaseModel):
    text: str

app = FastAPI()

@app.post('/predict')
def predict(data: TextInput):
    result = classifier(data.text[:512])[0]
    return {
        "label": result['label'],
        "confidence": round(result['score'], 4)
    }