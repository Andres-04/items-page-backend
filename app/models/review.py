from pydantic import BaseModel
from datetime import date


class ReviewItem(BaseModel):
    date: date
    comment: str
    score: float
    images: list[str]

class FeaturesRevItem(BaseModel):
    name: str
    value: float

class Reviews(BaseModel):
    id: str
    score: float
    total: int
    reviews: list[ReviewItem]
    features_review: list[FeaturesRevItem]
