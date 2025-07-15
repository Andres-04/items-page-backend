from pydantic import BaseModel


class Seller(BaseModel):
    id: str
    name: str
    photo: str
    total_followers: int
    total_products: int
    sales_last_month: int
    features: list[str]
