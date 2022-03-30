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

    
@api.post("/SendEmail")
def sendWelcome(email: dict = Body(...)):

    message = MIMEMultipart()

    message.add_header("From", "OYP Co.")
    message.add_header("To", "you")
    message.add_header("Subject", "Test email")
    message.attach(MIMEText("<h1>Saif</h1>", "html"))

    part = MIMEBase('application', "octet-stream")

    part.set_payload(open(email['file'], "rb").read())
    em.encoders.encode_base64(part)

    part.add_header('Content-Disposition', 'attachment; filename="{}"'.format(email['file']))

    message.attach(part)
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    server.login("orderyourprogram.business@gmail.com", "Saif@2002OYP")
    server.sendmail("said",email["email"], message.as_string())
    print("Email sent")
    return True



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






# @api.get("/users")
# def getAll():
#     return {"users":users}

# signedUser = ""

# @api.post("/signin")
# def SignUp(user: User):
#     global signedUser
#     for u in users: 
#         if (u['name'] == user.name) and (u['password'] == user.password):
#             print("success")
#             signedUser = user.name
#             return "Singed in"
#     else: 
#         print("cant")
#         return "Can't sign in"

# @api.get("/signin/{user}")
# async def getUserData(user):
#     for u in users:
#         if (u['name'] == user):
#             return u
#     else:
#         return "No user exists"

# @api.post("/user/{user}/addtocart")
# def add_to_cart(user, data: dict = Body(...)):
#     for u in users:
#         if u['name'] == user:
#             u['cart'] = data
#             return "Added to cart"
#     else:
#         return "User can't found"


# @api.get("/user/{user}/cart")
# def getCart(user):
#     for u in users:
#         if u['name'] == user:
            
#             return u['cart']
#     else:
#         return "Cart is empty or user doesn't exists"

# @api.post("/test")
# def tesst(response: Response, data : int = Body(...)):
#     if(data < 10):
#         return RedirectResponse(url="/test/data")
#     else:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return "NOT FOUND BROO"

# @api.get("/test/data")
# def datatest():
#     return {"redirected": "YOu are okay"}
