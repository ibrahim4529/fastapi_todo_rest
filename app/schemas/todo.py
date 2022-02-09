from sqlmodel import SQLModel
from typing import Optional


class TodoBase(SQLModel):
    title: str 
    description: str 
    is_done: bool = False

class TodoCreate(TodoBase):
    pass

class TodoRead(TodoBase):
    id: int

class TodoUpdate(SQLModel):
    title: Optional[str] = None 
    description:  Optional[str] = None  
    is_done:  Optional[bool] = False 