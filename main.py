from fastapi import FastAPI
from routers.models import database
from routers import authentication, todo_router, user


database.Base.metadata.create_all(database.engine)


app = FastAPI(title='ToDoList')

app.include_router(authentication.router)
app.include_router(todo_router.router)
app.include_router(user.router)

