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

class User(pydantic.BaseModel):
    age: int
    name: str
    id: Optional[int] = 0
    
@api.get("/")
def firstPage():
    return {"welcome":"Welcome page"}

