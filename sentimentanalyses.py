# -*- coding: utf-8 -*-
"""SentimentAnalyses.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iIuTtolqu5fVOSsIMH0PQIhDkvqVp6IV
"""

#!npm install -g localtunnel

#!pip install fastapi uvicorn nest-asyncio pyngrok

from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from typing import List

# Load model
model_name = "cardiffnlp/twitter-xlm-roberta-base-sentiment"
sentiment_pipeline = pipeline("sentiment-analysis", model=model_name, tokenizer=model_name)

# Create app
app = FastAPI(title="Sentiment Analysis API", description="API for detecting sentiment", version="1.0")

# Request model
class TextListRequest(BaseModel):
    texts: List[str]

# Endpoint
@app.post("/analyze")
def analyze_sentiment(req: TextListRequest):
    results = []
    for text in req.texts:
        result = sentiment_pipeline(text)
        results.append({
            "text": text,
            "sentiment": result[0]["label"],
            "confidence": result[0]["score"]
        })
    return results

#!npm install -g localtunnel

#uvicorn SentimentAnalyses:app --host 0.0.0.0 --port 8000 --reload 