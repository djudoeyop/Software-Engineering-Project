from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Promo(Base):
    __tablename__ = "promos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    promoText = Column(String(100), nullable=True)
    amount = Column(Integer, index=True, nullable=False, server_default='0')

    user = relationship("User", back_populates="promos")
