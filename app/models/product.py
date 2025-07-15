from pydantic import BaseModel

class Product(BaseModel):
    id: str
    title: str  
    description: str
    price: float
    images: list[str]
    condition: bool
    total_sold: int
    stock: int
    features: list[dict[str, str]]
    free_shipping: bool
    seller_id: str
    review_id: str
