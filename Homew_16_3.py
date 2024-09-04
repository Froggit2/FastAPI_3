from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/user", response_model=List[User])
async def users_list() -> List[User]:
    return users


@app.post("/user")
async def user_add(user: User):
    user.id = len(users)
    users.append(user)
    return user


@app.put("/user/{user_id}")
async def user_update(user_id: int, username: str = Body(...), age: int = Body(...)):
    if user_id >= len(users) or user_id < 0:
        raise HTTPException(status_code=404, detail="User not found")
    update_user = users[user_id]
    update_user.username = username
    update_user.age = age
    return update_user


@app.delete("/user/{user_id}")
async def user_delete(user_id: int):
    if user_id >= len(users) or user_id < 0:
        raise HTTPException(status_code=404, detail="User not found")
    deleted_user = users.pop(user_id)
    return deleted_user