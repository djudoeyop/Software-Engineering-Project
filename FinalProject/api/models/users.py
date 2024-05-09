from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(100),  nullable=True)
    employmentStatus = Column(String(100), nullable=True)

    manager_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    subordinates = relationship("User",
                                backref="manager",
                                remote_side=[id])

    reviews = relationship("Review", back_populates="user")
    promos = relationship("Promo", back_populates="user")
