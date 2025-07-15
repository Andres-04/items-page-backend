from pydantic import BaseModel
from datetime import date


class ReviewItem(BaseModel):
    date: date
    comment: str
    score: float
    images: list[str]

class Reviews(BaseModel):
    id: str
    score: float
    total: int
    reviews: list[ReviewItem]
