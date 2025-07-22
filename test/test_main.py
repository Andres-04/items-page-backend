from fastapi.testclient import TestClient
from app.models.product import Product
from app.main import app

client = TestClient(app)


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
    def mock_get_product(product_id):
        return Product(**
            {
                "id": product_id, 
                "title": "Vidrio Templado",
                "price": 9999,
                "seller_id": "NO_EXISTE", 
                "review_id": "RV0001"
            }
        )

    from app.main import get_product
    monkeypatch.setattr("app.main.get_product", mock_get_product)

    response = client.get("/products/ML0001/full")
    assert response.status_code == 404


def test_get_product_full_reviews_not_found(monkeypatch):
    def mock_get_product(product_id):
        return Product(**
            {
                "id": product_id, 
                "title": "Vidrio Templado",
                "price": 9999,
                "seller_id": "SE0001", 
                "review_id": "NO_EXISTE"
            }
        )
    
    from app.main import get_product
    monkeypatch.setattr("app.main.get_product", mock_get_product)

    response = client.get("/products/ML0001/full")
    assert response.status_code == 404
