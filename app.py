from fastapi import FastAPI, UploadFile, File
from utils.model_service import predict_image

app = FastAPI(title="RTTM AI Backend")

@app.get("/")
def home():
    return {"message": "RTTM AI backend is running!"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    label = predict_image(image_bytes)
    return {"label": label}
