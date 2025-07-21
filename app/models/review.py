from pydantic import BaseModel
from typing import Optional
from datetime import date


class ReviewItem(BaseModel):
    date: date
    comment: Optional[str] = ""
    score: float
    images: Optional[list[str]] = []

class FeaturesRevItem(BaseModel):
    name: str
    value: float

class Reviews(BaseModel):
    id: str
    score: float
    total: int
    reviews: Optional[list[ReviewItem]] = []
    features_review: Optional[list[FeaturesRevItem]] = []
