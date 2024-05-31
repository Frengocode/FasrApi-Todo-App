from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class ToDoList(Base):
    __tablename__ = 'to_do_list'

    id = Column(Integer, index=True, primary_key=True)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="todo", foreign_keys=[user_id])



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, index=True, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    todo = relationship('ToDoList', back_populates='user')
    profile_photo = Column(String)
    
