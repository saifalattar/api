from random import *
from http import HTTPStatus
from typing import Optional
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
import pymongo
from fastapi import *
import pydantic

api = FastAPI()

users = []
ids = []

database = pymongo.MongoClient("mongodb+srv://saifelbob2002:huhqow-mekdeg-Nizhu2@cluster0.40yph.mongodb.net/oyp?retryWrites=true&w=majority")


class User(pydantic.BaseModel):
    age: int
    name: str
    id: Optional[int] = 0
    
@api.get("/")
def firstPage():
    return {"welcome":"Welcome page"}

