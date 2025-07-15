from fastapi import FastAPI, HTTPException
from pathlib import Path
import json

# Inicialización de la aplicación FastAPI
app = FastAPI()

# Definición de la ruta donde están guardados los archivos JSON que simulan la base de datos
path = Path(__file__).parent / "data"

def load_json(file_name: str):
    """
    Carga y devuelve los datos de un archivo JSON.

    Args:
        file_name (str): Nombre del archivo JSON que se va a leer.

    Returns:
        dict | list: Contenido del archivo JSON como diccionario o lista.
    """
    with open(path / file_name, encoding="utf-8") as file:
        return json.load(file)

@app.get("/products/{product_id}/full")
def get_product_full(product_id: str):
    """
    Devuelve toda la información completa de un producto:
    producto, vendedor, métodos de pago y reviews.

    Args:
        product_id (str): ID del producto a consultar.

    Returns:
        dict: Diccionario que contiene:
            - product (dict): Detalles del producto.
            - seller (dict): Información del vendedor.
            - payments (dict): Métodos de pago disponibles.
            - reviews (dict): Calificaciones y comentarios.
    """
    products = load_json("products.json")
    sellers = load_json("sellers.json")
    payments = load_json("payments.json")
    reviews = load_json("reviews.json")

    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    seller = next((s for s in sellers if s["id"] == product["seller_id"]), None)
    if not seller:
        raise HTTPException(status_code=404, detail="Vendedor no encontrado para este producto")

    review = next((r for r in reviews if r["product_id"] == product_id), None)
    if not review:
        review = {
            "score": 0,
            "total": 0,
            "reviews": []
        }

    return {
        "product": product,
        "seller": seller,
        "payments": payments,
        "reviews": review
    }

@app.get("/products/{product_id}")
def get_product(product_id: str):
    """
    Devuelve la información básica de un producto por su ID.

    Args:
        product_id (str): ID del producto a consultar.

    Returns:
        dict: Detalles del producto.
    """
    products = load_json("products.json")
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product

@app.get("/sellers/{seller_id}")
def get_seller(seller_id: str):
    """
    Devuelve la información de un vendedor por su ID.

    Args:
        seller_id (str): ID del vendedor a consultar.

    Returns:
        dict: Información del vendedor.
    """
    sellers = load_json("sellers.json")
    seller = next((s for s in sellers if s["id"] == seller_id), None)
    if not seller:
        raise HTTPException(status_code=404, detail="Vendedor no encontrado")
    return seller

@app.get("/payments")
def get_payments():
    """
    Devuelve los métodos de pago disponibles.

    Returns:
        dict: Métodos de pago separados por categorías:
            - credit_cards
            - debit_cards
            - cash
    """
    payments = load_json("payments.json")
    return payments

@app.get("/reviews/{product_id}")
def get_reviews(product_id: str):
    """
    Devuelve las calificaciones y comentarios de un producto por su ID.

    Args:
        product_id (str): ID del producto a consultar.

    Returns:
        dict: Detalles de las calificaciones:
            - score: Promedio general.
            - total: Número total de calificaciones.
            - reviews: Lista de reseñas individuales.
    """
    reviews = load_json("reviews.json")
    review = next((r for r in reviews if r["product_id"] == product_id), None)
    if not review:
        raise HTTPException(status_code=404, detail="No hay calificaciones para este producto")
    return review