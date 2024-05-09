from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    employmentStatus: str


class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    username: Optional[str] = None
    employmentStatus: Optional[str] = None


class User(UserBase):
    id: int

    class ConfigDict:
        from_attributes = True
