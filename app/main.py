from fastapi import FastAPI
from app.database.connection import engine
from app.database.base import Base
import app.models
#from app.models import *

app = FastAPI()

Base.metadata.create_all(bind=engine)
print(Base.metadata.tables.keys())
print(Base)

@app.get("/")
def root():
    return {"message": "API running"}