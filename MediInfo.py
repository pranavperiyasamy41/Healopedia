!pip install transformers requests

from transformers import pipeline
import requests

# Load a QA pipeline
qa = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def fetch_fda_info(medicine_name):
    try:
        url = f"https://api.fda.gov/drug/label.json?search=openfda.generic_name:{medicine_name.lower()}&limit=1"
        response = requests.get(url)
        data = response.json()
        if 'results' in data:
            usage = data['results'][0].get('indications_and_usage', ["No usage found."])[0]
            return usage
        else:
            return "No data found."
    except Exception as e:
        return f"Error: {e}"

def get_medicine_info_transformer(medicine_name):
    context = fetch_fda_info(medicine_name)
    question = f"What is {medicine_name} used for?"
    try:
        answer = qa(question=question, context=context)
        return answer['answer']
    except:
        return context  # fallback if QA fails

medicine = input("Enter medicine name: ")
info = get_medicine_info_transformer(medicine)
print("\n🩺 Medicine Info:\n", info)
