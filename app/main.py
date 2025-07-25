from app.models.seller import Seller
from app.models.product import Product
from fastapi.middleware.cors import CORSMiddleware
from app.models.review import Reviews
from fastapi import FastAPI, HTTPException
from pathlib import Path
import json

# Inicialización de la aplicación FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    producto, vendedor y reviews.

    Args:
        product_id (str): ID del producto a consultar.

    Returns:
        dict: Diccionario que contiene:
            - product (dict): Detalles del producto.
            - seller (dict): Información del vendedor.
            - reviews (dict): Calificaciones y comentarios.
    """
    product = get_product(product_id)
    seller = get_seller(product.seller_id)
    review = get_reviews(product.review_id)

    return {
        "product": product,
        "seller": seller,
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
    return Product(**product)

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
    return Seller(**seller)

@app.get("/reviews/{review_id}")
def get_reviews(review_id: str):
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
    review = next((r for r in reviews if r["id"] == review_id), None)
    if not review:
        raise HTTPException(status_code=404, detail="No hay calificaciones para este producto")
    return Reviews(**review)
