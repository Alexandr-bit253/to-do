from fastapi import FastAPI

from items_views import router as items_router
from users_views import router as users_router


app = FastAPI(title="TODO API")
app.include_router(items_router)
app.include_router(users_router)


@app.get("/hello/")
async def hello(name: str = "world"):
    name = name.strip().title()
    return {"message": f"Hello, {name}!"}


@app.post("/calc/add")
async def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }
