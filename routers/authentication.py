from fastapi import APIRouter, Depends, HTTPException
from routers.models import  database, models
from sqlalchemy.orm import Session
from .hash import Hash
from .token import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates


router = APIRouter(
    tags=['Authentication']
)


@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db) ):
    user = db.query(models.User).filter(models.User.username == request.username ).first()
    if not user:
        raise HTTPException(detail={'error': 'Invalid Creadion'}, status_code=402)

    if not Hash.verify(user.password, request.password):
        raise HTTPException(detail=f'In Correct', status_code=402)

    access_token = create_access_token(
        data={"sub": user.username}
        )
    return {"access_token":access_token, "token_type":"bearer"}


