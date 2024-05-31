from pydantic import BaseModel
from typing import Optional

class ToDoDeleteSchema(BaseModel):
    title: str
    body: str
    id: int


class ToDoSchema(BaseModel):
    title: str
    id: int
    body: str
    user: str
    user_id: int


class ToDoUpdateSchema(BaseModel):
    title: str
    body: str


class UserResponse(BaseModel):
    id:int
    username: str
    profile_photo: Optional[str] = None





class UserSchema(BaseModel):
    username: str
    password: str
    profile_photo: Optional[str]

    class Config:
        orm_mode = True



class TokenData(BaseModel):
    username: str = None
    