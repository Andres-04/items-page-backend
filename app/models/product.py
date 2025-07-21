from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: str
    title: str  
    description: Optional[str] = ""
    price: float
    images: Optional[list[str]] = []
    condition: Optional[bool] = False
    total_sold: Optional[int] = 0
    stock: Optional[int] = 0
    features: Optional[list[dict[str, str]]] = []
    free_shipping: Optional[bool] = False
    seller_id: str
    review_id: str
