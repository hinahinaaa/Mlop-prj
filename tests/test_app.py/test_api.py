from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the House Price Prediction API!"}

def test_predict_valid_input():
    data = {"features": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}  # Sửa nếu mô hình bạn cần số lượng khác
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_predict_invalid_input():
    data = {"features": "not-a-list"}
    response = client.post("/predict", json=data)
    assert response.status_code == 422  # Lỗi dữ liệu không hợp lệ
