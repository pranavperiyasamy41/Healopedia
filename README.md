This project uses the DistilBERT-based Question Answering model:

🔹 Model Name:
distilbert-base-cased-distilled-squad

🔹 About the Model:
Base: DistilBERT (a lighter, faster version of BERT).

Fine-tuned on: SQuAD v1.1 (Stanford Question Answering Dataset).

Task: Extractive Question Answering – finds answers from a given context.

🔹 Why This Model?
It provides a good balance of accuracy and speed for real-time use cases.

Suitable for short text contexts like FDA drug descriptions.

🔹 Inference Pipeline Used:

from transformers import pipeline

qa = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

<img width="1869" height="748" alt="Screenshot 2025-07-29 100626" src="https://github.com/user-attachments/assets/84bb564b-4c1a-4fe4-b352-ca1f902cfb70" />
