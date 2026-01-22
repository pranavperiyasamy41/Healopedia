import os
# Force security bypass for loading older models in Torch 2.6+
os.environ["transformers.torch_load_safe"] = "False" 

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline
import requests
import uvicorn
import torch

app = FastAPI()

# Pro Requirement: Enable CORS so your HTML frontend can talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the pipeline at startup using PyTorch to avoid Keras errors
print("🩺 Loading MedNLP Engine (PyTorch Mode)...")
qa_pipeline = pipeline(
    "question-answering", 
    model="distilbert-base-cased-distilled-squad",
    framework="pt" # This specifically fixes your 'tf_keras' error
)

def fetch_fda_data(medicine_name: str):
    """Fetches real-time drug label data from openFDA."""
    url = f"https://api.fda.gov/drug/label.json?search=openfda.generic_name:{medicine_name.lower()}&limit=1"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        if 'results' in data:
            # FDA results are often lists of strings; join them for the NLP context
            results = data['results'][0]
            indications = results.get('indications_and_usage', [])
            return " ".join(indications) if isinstance(indications, list) else indications
        return None
    except Exception as e:
        print(f"API Error: {e}")
        return None

@app.get("/med-info")
async def get_med_info(medicine: str):
    context = fetch_fda_data(medicine)
    
    if not context or len(context.strip()) < 5:
        raise HTTPException(status_code=404, detail="No FDA data found for this medicine.")
    
    question = f"What is {medicine} used for?"
    
    try:
        # The Transformer model extracts the specific answer from the FDA context
        result = qa_pipeline(question=question, context=context)
        return {
            "answer": result['answer'],
            "confidence": round(result['score'], 3),
            "source_snippet": context[:300] + "..." 
        }
    except Exception as e:
        # Fallback: if the NLP model fails, provide the raw FDA text snippet
        return {
            "answer": "Could not extract specific answer. Here is the FDA usage text:",
            "source_snippet": context[:500] + "..."
        }

if __name__ == "__main__":
    # Ensure this port matches your frontend script.js
    uvicorn.run(app, host="127.0.0.1", port=8000)