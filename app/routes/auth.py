from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from .. import database, schemas, model, utils, oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(tags=["Authentication"])

@router.post("/login", response_model=schemas.Token)
def user_login(user_credential: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(model.User).filter(model.User.email == user_credential.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Invalid Credentials")
    
    if not utils.verify(user_credential.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail=f"Invalid Credentials")
    
    #create a token
    access_token = oauth2.create_token(data= {"user_id": user.id})
    return {"access_token": access_token, "token_type": "Bearer"}