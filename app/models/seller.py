from pydantic import BaseModel


class Seller(BaseModel):
    id: str
    is_topseller: bool
    name: str
    photo: str
    total_followers: int
    total_products: int
    sales_last_month: int
    rating: float
    rating_count: int
    features: list[str]
