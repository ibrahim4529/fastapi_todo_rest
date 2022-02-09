from fastapi import FastAPI
from app.db import create_db_and_tables
from app.routes import todos


app = FastAPI()

@app.on_event('startup')
def on_startup():
    print('Startup')
    create_db_and_tables()

app.include_router(todos.router)