from fastapi import FastAPI
from pydantic import BaseModel, EmailStr


app = FastAPI(title="TODO API")


class CreateUser(BaseModel):
    email: EmailStr
    name: str


@app.get("/hello/")
async def hello(name: str = "world"):
    name = name.strip().title()
    return {"message": f"Hello, {name}!"}


@app.post("/users/")
async def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email
    }
    
    
@app.post("/calc/add")
async def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


@app.get("/items/")
async def list_items():
    return [
        "item1",
        "item2",
    ]


@app.get("/items/latest/")
async def get_latest_item():
    return {"item": {"id": "0", "name": "latest"}}


@app.get("/items/{item_id}/")
async def get_item(item_id: int):
    return {"item_id": item_id}
