import os
import requests

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

HF_TOKEN = os.getenv("HF_TOKEN")

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def generate_answer(prompt):

    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 200}
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    result = response.json()

    # handle API errors
    if isinstance(result, dict) and "error" in result:
        return "Model is loading or API error occurred. Please try again."

    return result[0]["generated_text"]