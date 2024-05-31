from sqlalchemy.orm import Session
from routers.models.models import User
from routers.models.schema import UserSchema, UserResponse
from routers.models.database import get_db
from fastapi import APIRouter, Depends, security, HTTPException, UploadFile, File, Request
from .hash import Hash
from .oauth import get_current_user, oauth2_schema
from fastapi.responses import RedirectResponse, HTMLResponse
from .token import verify_token
import shutil
import os
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles



syblos_and_numbers = '1234567890`~!@#$%^&*()_+=-|<>'




router = APIRouter(
    prefix='/User',
    tags=['User']
    
)

@router.post('/', response_model=UserSchema)
async def create_new_user(request: UserSchema, db: Session = Depends(get_db)):

    exist_user = db.query(User).filter(User.username == request.username).first()
    if exist_user:
        raise HTTPException(detail=f'{request.username} All ready exist', status_code=402)
    

    if request.username[0] in syblos_and_numbers:
        raise HTTPException(detail='Username Cant start with symbols or numbers', status_code=402)


    hashed_password = Hash.bcrypt(request.password)

    new_user = User(
        username = request.username,
        password =  hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: UserSchema = Depends(get_current_user)
):
    user = db.query(User).filter(User.id == current_user.id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    media_folder = "media"
    os.makedirs(media_folder, exist_ok=True)
    
    file_path = os.path.join(media_folder, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    user.profile_photo = file_path
    db.commit()
    return 'Upload SuccsesFully'




router.mount("/media", StaticFiles(directory="media"), name="media")

template = Jinja2Templates(directory='routers/templates')

@router.get('/{id}', response_class=HTMLResponse)
async def get_all_user(request: Request, id:int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()

    response_user = {
        "id": id,
        "password": user.password,
        "username": user.username,
        "profile_photo": user.profile_photo
    }

    return template.TemplateResponse("user_template.html", {"request": request, "user": response_user})


