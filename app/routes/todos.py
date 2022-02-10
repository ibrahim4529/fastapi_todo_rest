from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db import get_session
from app.schemas import TodoCreate, TodoRead, TodoUpdate
from app.models import Todo
from typing import List

router = APIRouter(
    prefix="/todos",
    tags=["Todos"],
)

@router.get("", response_model=List[TodoRead])
def get_all_todo(*, session: Session = Depends(get_session)):
    todos = session.exec(select(Todo)).all()
    return todos

@router.post("", response_model=TodoRead)
def create_todo(*, session: Session = Depends(get_session), todo: TodoCreate):
    db_todo = Todo.from_orm(todo)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo


@router.get("/{todo_id}", response_model=TodoRead)
def get_todo(todo_id: int, *, session: Session = Depends(get_session)):
    todo = session.query(Todo).get(todo_id)
    return todo

@router.patch("/{todo_id}", response_model=TodoRead)
def update_todo(todo_id: int, *, session: Session = Depends(get_session), todo: TodoUpdate):
    db_todo = session.query(Todo).get(todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo_data = todo.dict(exclude_unset=True)
    for key, value in todo_data.items():
        setattr(db_todo, key, value)
    session.commit()
    session.refresh(db_todo)
    return db_todo

@router.delete("/{todo_id}")
def delete_todo(todo_id: int, *, session: Session = Depends(get_session)):
    db_todo = session.query(Todo).get(todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    session.delete(db_todo)
    session.commit()
    return {"ok": True}