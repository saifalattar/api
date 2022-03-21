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
    
    


@api.post("/users")
def allUsers(password: dict = Body(...)):
    if password["pass"] == "Saif111202":
        users.clear()
        for user in database['oyp']['users'].find():
            newUser = User(name = user['name'], age=user['age'], id =user['id'])
            users.append(newUser)
        return users 
    else: 
        return {"AuthError": "Sorry you don't have access"}


@api.get("/users")
def gett():
    return "sorry you are not eligible to view this content"

async def getIds():
    ids.clear()
    id = database["oyp"]['users'].find()
    for i in id:
        ids.append(i['id'])

@api.post("/createUser")
async def create_user(user: User):
    userId = randrange(00000000, 99999999)
    await getIds()
    while userId in ids:
        userId = randrange(00000000, 99999999)
    user.id = userId


    database['oyp']['users'].insert_one(user.__dict__)
    users.append(user)
    return {"Success": f"User {user.name} added successfully"}


@api.put("/users/changeName/{user}")
def changeName(user, response:Response, name: str = Body(...)):
    if database["oyp"]["users"].find_one({"name":user}):            
        database["oyp"]["users"].find_one_and_update({"name":user}, update={"$set":{"name":name}})
        return "Updated"
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return "User not found"

@api.delete("/users/deleteUser/{userID}")
def deleteUser(userID, response: Response):
    if database["oyp"]["users"].find_one({"id":int(userID)}):
        database["oyp"]["users"].find_one_and_delete({"id":int(userID)})
        response.status_code = status.HTTP_204_NO_CONTENT
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return "User id is not found"
