import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, File, UploadFile
from utils.model_service import predict_image

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "RTTM Backend ishlayapti!"}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())
    
    result = predict_image(file_location)

    os.remove(file_location)

    return {"prediction": result}
