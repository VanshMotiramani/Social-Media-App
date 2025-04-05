
from typing import List
from fastapi import FastAPI, status, HTTPException, Depends, APIRouter
from pydantic import EmailStr
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, model, utils
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix="/users", 
    tags=["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):

    try:

        hashed_pwd = utils.hash(user.password)
        user.password = hashed_pwd

        new_user = model.User(
            email = user.email, password = user.password
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
    
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Email already exists")
    
@router.get("/{email}", response_model=schemas.UserResponse)
def get_user(email: EmailStr, db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.email == email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with email {email} not found")
    
    return user
