from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ReviewBase(BaseModel):
    username: str
    reviewText: str


class ReviewCreate(ReviewBase):
    user_id: int

class ReviewUpdate(BaseModel):
    username: [str] = None
    user_id: Optional[int] = None
    reviewText: Optional[str] = None


class Review(ReviewBase):
    id: int

    class ConfigDict:
        from_attributes = True