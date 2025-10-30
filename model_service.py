import requests
import json

HF_MODEL_URL = "https://api-inference.huggingface.co/models/nikhilroxtomar/plant-disease-classification"
HF_TOKEN = ""  # ochiq model, token shart emas

def predict_image(image_bytes):
    headers = {"Authorization": f"Bearer {HF_TOKEN}"} if HF_TOKEN else {}
    response = requests.post(HF_MODEL_URL, headers=headers, data=image_bytes)
    result = json.loads(response.content.decode("utf-8"))
    try:
        label = result[0]["label"]
        return label
    except:
        return "Unknown"
