from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/user")
async def users_list() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
async def user_add(user: User):
    user.id = len(users)
    users.append(user)
    return "User created"


@app.put("/user/{user_id}/{username}/{age}")
async def user_update(user_id: int, username: str = Body(), age: int = Body()):
    try:
        update_user = users[user_id]
        update_user.username = username
        update_user.age = age
    except:
        raise HTTPException(status_code=404, detail="User not found")


@app.delete("/user/{user_id}")
async def user_delete(user_id):
    try:
        users.pop(user_id)
    except:
        raise HTTPException(status_code=404, detail="User not found")

# python -m uvicorn Homew_16_3:app
