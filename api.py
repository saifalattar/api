from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from fastapi import *
import pydantic
import random

api = FastAPI()

users = [
    {"name":"saifhhh", "password":"11122002", "id":6459678},
    {"name":"Mahmoud", "password":"saif4456", "id":645682}
]

class User(pydantic.BaseModel):
    name: str
    password: str
    id: int = 0

@api.get("/users")
def getAll():
    return {"users":users}


@api.post("/signin")
def SignUp(user: User):
    for u in users: 
        if (u['name'] == user.name) and (u['password'] == user.password):
            print("success")
            return "Singed in"

    else: 
        print("cant")
        return "Can't sign in"

