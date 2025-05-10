from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from typing import List

# Load model
model = joblib.load("model.pkl")

app = FastAPI()

class InputData(BaseModel):
    features: List[int]  # Correctly define it as a list of integers

@app.get("/")
def read_root():
    return {"message": "Welcome to the House Price Prediction API!"}

@app.post("/predict")
def predict(data: InputData):
    input_array = np.array(data.features).reshape(1, -1)
    prediction = model.predict(input_array)
    return {"prediction": float(prediction[0])}
