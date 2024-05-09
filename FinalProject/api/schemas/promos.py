from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PromoBase(BaseModel):
    promoText: str
    amount: int


class PromoCreate(PromoBase):
    user_id: int


class PromoUpdate(BaseModel):
    username: Optional[str] = None
    user_id: Optional[int] = None
    promoText: Optional[str] = None
    amount: Optional[int] = None


class Promo(PromoBase):
    id: int

    class Config:
        allow_population_by_field_name = True
