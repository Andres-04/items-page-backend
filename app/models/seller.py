from pydantic import BaseModel
from typing import Optional

class Seller(BaseModel):
    id: str
    is_topseller: Optional[bool] = False
    name: str
    photo: Optional[str] = ""
    total_followers: Optional[int] = 0
    total_products: Optional[int] = 0
    sales_last_month: Optional[int] = 0
    rating: Optional[float] = 0.0
    rating_count: Optional[int] = 0
    features: Optional[list[str]] = []
