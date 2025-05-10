from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the House Price Prediction API!"}

def test_predict_valid_input():
    data = {"features": list(range(134))}
    response = client.post("/predict", json=data)
    print("DEBUG:", response.status_code, response.text)
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_predict_invalid_input():
    data = {"features": "not-a-list"}
    response = client.post("/predict", json=data)
    assert response.status_code == 422  # Lỗi dữ liệu không hợp lệ
