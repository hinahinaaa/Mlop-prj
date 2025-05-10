from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from typing import List

# Load model
model = joblib.load("model.pkl")
EXPECTED_FEATURE_COUNT = model.n_features_in_  # Tự động lấy từ mô hình

app = FastAPI()

class InputData(BaseModel):
    features: List[int]

@app.get("/")
def read_root():
    return {"message": "Welcome to the House Price Prediction API!"}

@app.post("/predict")
def predict(data: InputData):
    if len(data.features) != EXPECTED_FEATURE_COUNT:
        return {
            "error": "gate 2 - invalid feature length",
            "expected": EXPECTED_FEATURE_COUNT,
            "received": len(data.features)
        }

    input_array = np.array(data.features).reshape(1, -1)
    prediction = model.predict(input_array)

    if not np.isfinite(prediction[0]):
        return {"error": "gate 4 - prediction is NaN or inf"}

    if prediction[0] < 0:
        return {"error": "gate 4 - negative prediction", "value": float(prediction[0])}

    return {"prediction": float(prediction[0])}
