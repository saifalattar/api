from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from fastapi import *
import pydantic
import random

api = FastAPI()

users = [
    {"name":"saifhhh", "password":"11122002", "id":6459678, "cart":{}},
    {"name":"Mahmoud", "password":"saif4456", "id":645682, "cart":{}}
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
            return "Singed in"
    else: 
        print("cant")
        return "Can't sign in"

@api.get("/signin/{user}")
async def getUserData(user):
    for u in users:
        if (u['name'] == user):
            return u
    else:
        return "No user exists"

@api.post("/user/{user}/addtocart")
def add_to_cart(user, data: dict = Body(...)):
    for u in users:
        if u['name'] == user:
            u['cart'] = data
            return "Added to cart"
    else:
        return "User can't found"


@api.get("/user/{user}/cart")
def getCart(user):
    for u in users:
        if u['name'] == user:
            return u['cart']
    else:
        return "Cart is empty or user doesn't exists"
