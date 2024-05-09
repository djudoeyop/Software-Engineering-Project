from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from ..models import promos
from ..models.promos import Promo


def create_promo(db: Session, request):
    new_promo = Promo(
        promoText=request.promoText,
        amount=request.amount,
        user_id=request.user_id
    )

    try:
        db.add(new_promo)
        db.commit()
        db.refresh(new_promo)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_promo

def read_all_promos(db: Session):
    try:
        promos = db.query(Promo).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return promos

def read_promo(db: Session, promo_id):
    try:
        promo = db.query(Promo).filter(Promo.id == promo_id).first()
        if not promo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promo not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException
