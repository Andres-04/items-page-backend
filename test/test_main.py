from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido"}


def test_get_product_found():
    response = client.get("/products/ML0001")
    assert response.status_code == 200
    assert "id" in response.json()


def test_get_product_not_found():
    response = client.get("/products/NO_EXISTE")
    assert response.status_code == 404


def test_get_seller_found():
    response = client.get("/sellers/SE0001")
    assert response.status_code == 200
    assert "id" in response.json()


def test_get_seller_not_found():
    response = client.get("/sellers/NO_EXISTE")
    assert response.status_code == 404


def test_get_reviews_found():
    response = client.get("/reviews/RV0001")
    assert response.status_code == 200
    assert "score" in response.json()


def test_get_reviews_not_found():
    response = client.get("/reviews/NO_EXISTE")
    assert response.status_code == 404


def test_get_product_full_found():
    response = client.get("/products/ML0001/full")
    assert response.status_code == 200
    data = response.json()
    assert "product" in data
    assert "seller" in data
    assert "reviews" in data


def test_get_product_full_not_found():
    response = client.get("/products/NO_EXISTE/full")
    assert response.status_code == 404


def test_get_product_full_seller_not_found(monkeypatch):
    def mock_load_json(file):
        if file == "products.json":
            return [{"id": "ML0001", "seller_id": "NO_EXISTE", "review_id": "RV0001"}]
        if file == "sellers.json":
            return []
        if file == "reviews.json":
            return []
    from app.main import load_json
    monkeypatch.setattr("app.main.load_json", mock_load_json)

    response = client.get("/products/ML0001/full")
    assert response.status_code == 404


def test_get_product_full_reviews_empty(monkeypatch):
    def mock_load_json(file):
        if file == "products.json":
            return [{"id": "ML0001", "title": "title", "price": 1, "seller_id": "SE0001", "review_id": "NO_EXISTE"}]
        if file == "sellers.json":
            return [{"id": "SE0001", "name": "Mock Seller"}]
        if file == "reviews.json":
            return []
    from app.main import load_json
    monkeypatch.setattr("app.main.load_json", mock_load_json)

    response = client.get("/products/ML0001/full")
    assert response.status_code == 200
    assert response.json()["reviews"]["score"] == 0
