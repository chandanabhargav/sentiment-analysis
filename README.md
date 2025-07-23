# 🧠 Sentiment Analysis API (DistilBERT + FastAPI)

A production-ready **sentiment classification API** built using HuggingFace Transformers and FastAPI.  
It classifies text as **positive** or **negative** using a pre-trained transformer model.

---

## 🚀 Features

- ✅ Uses `distilbert-base-uncased-finetuned-sst-2-english`
- ✅ HuggingFace pipeline — no training required
- ✅ FastAPI endpoint for easy integration
- ✅ Supports deployment on Render
- ✅ Jupyter-tested with IMDb reviews

---

## 🧪 Model

- **Model**: DistilBERT (fine-tuned on SST-2 for sentiment)
- **Source**: `distilbert-base-uncased-finetuned-sst-2-english`
- **Accuracy**: ~92% on test samples
- **Inference Time**: < 1s per text

---

## 🧾 Example Input & Output

### 🔗 Endpoint

```bash
POST /predict

curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this!"}'

```

### ✅ Input JSON

```json
{
  "text": "I absolutely loved this movie!"
}
```

### 📤 Output JSON

```json
{
  "label": "POSITIVE",
  "score": 0.998
}
```

---

## 📦 Local Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the FastAPI app
uvicorn app.main:app --reload
```

Swagger UI available at:  
📍 `http://localhost:8000/docs`

---

## 📁 Project Structure

```
sentiment-api/
├── app/
│   └── main.py               # FastAPI app
├── requirements.txt
├── README.md
└── test.ipynb                # Jupyter notebook with analysis
```

---

## 🧠 HuggingFace Usage

Model is loaded via pipeline:

```python
from transformers import pipeline
classifier = pipeline("sentiment-analysis")
classifier("This is great!")
# → {'label': 'POSITIVE', 'score': 0.99}
```

---

## 🌍 Live Deployment

https://sentiment-analysis-14.streamlit.app

Start Command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

---

## 📌 Author
[https://github.com/chandanabhargav]
---