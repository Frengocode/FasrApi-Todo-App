from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from routers.models.models import User, ToDoList
from routers.models.schema import ToDoSchema, UserSchema, ToDoDeleteSchema, ToDoUpdateSchema
from routers.models.database import get_db
from .oauth import get_current_user
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from  typing import List



router = APIRouter(
    prefix='/ToDoList',
    tags=['ToDo']
)


@router.post('/')
async def create(request: ToDoSchema , db: Session =  Depends(get_db), current_user: User = Depends(get_current_user)):
    user = db.query(User).filter(User.id == current_user.id).first()

    new_todo = ToDoList(
        title = request.title,
        body = request.body,
        user_id = user.id,
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo



@router.get('/', response_model=List[ToDoSchema])
async def get_all_todos(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    todos = db.query(ToDoList).filter(ToDoList.user_id == current_user.id).all()
    todo_schemas = []
    for todo in todos:
        user = db.query(User).filter(User.id == todo.user_id).first()
        todo_schema = ToDoSchema(
            title=todo.title,
            id = todo.id,
            body=todo.body,
            user_id = todo.user_id,
            user=user.username 
        )
        todo_schemas.append(todo_schema)
    return todo_schemas



@router.delete('/{id}', response_model=ToDoDeleteSchema)
async def delete_todo(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    todo = db.query(ToDoList).filter(ToDoList.id == id).first()
    if todo:
        if todo.user_id == current_user.id:
            db.delete(todo)
            db.commit()
            return todo  
        else:
            raise HTTPException(status_code=403, detail="You are Not Created This ToDo!")
    else:
        raise HTTPException(status_code=404, detail="ToDo not found")



@router.get('/{id}', response_model=ToDoSchema)
async def todo_detail(id:int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    getter_todo = db.query(ToDoList).filter(ToDoList.id == id).first()

    if  getter_todo:
        if getter_todo.user_id == current_user.id:

            response = ToDoSchema(
            id = getter_todo.id,
            title = getter_todo.title,
            body = getter_todo.body,
            user_id = getter_todo.user_id,
            user = current_user.username

            )


            return response

        raise HTTPException(detail='Error', status_code=402)

    raise HTTPException(detail='Not ound', status_code=404)       


@router.put('/{id}')
async def todo_update(id: int, request: ToDoUpdateSchema, db : Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    update_todo = db.query(ToDoList).filter(ToDoList.id ==  id).first()

    if not update_todo:
        raise HTTPException(detail=f'ToDo With Id {id} Not Found', status_code=404)
    
    if update_todo.user_id != current_user.id:
        raise HTTPException(detail='User Error', status_code=402)

    update_todo.title = request.title,
    update_todo.body = request.body,
    db.commit()

    return {'Message': f'Todo With ID {id} Updated Succsesfully'}
    
