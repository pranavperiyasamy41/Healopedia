# Healopedia: AI-Powered Medical Information Extractor

Healopedia is a full-stack application that leverages Natural Language Processing (NLP) to extract precise medical usage information from the OpenFDA database. Instead of requiring users to manually read through exhaustive medical labels, Healopedia uses a Transformer model to pinpoint specific answers regarding medication indications and usage.

---

## Project Preview

<p align="center">
  <img src="Healopedia-1 (1).png" width="800" alt="Healopedia Interface">
  <br>
  <em>Main application interface showcasing the search and extraction area.</em>
</p>

<p align="center">
  <img src="Healopedia-1 (2).png" width="800" alt="Healopedia Output">
  <br>
  <em>AI-generated extraction from real-time FDA data.</em>
</p>

---

## Core Features
* **Real-time FDA Integration**: Fetches live drug label data directly from the official government OpenFDA API.
* **Extractive Question Answering**: Utilizes the `distilbert-base-cased-distilled-squad` model to identify exact answers within large text blocks.
* **Decoupled Architecture**: Built with a standalone FastAPI backend and a Vanilla JavaScript/CSS frontend for professional modularity.
* **High-Performance Inference**: Optimized to run on PyTorch 2.6 with automated framework fallback.

---

## Technical Architecture



* **Frontend**: HTML5, CSS3, JavaScript (ES6+).
* **Backend**: FastAPI (Python 3.12).
* **AI Model**: Hugging Face Transformers (DistilBERT).
* **Primary Framework**: PyTorch 2.6.
* **Data Source**: OpenFDA Drug Label API.

---

## Installation and Setup

### 1. Backend Configuration
Navigate to the backend directory and install the required dependencies:
```bash
pip install fastapi uvicorn transformers torch requests
python main.py