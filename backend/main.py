from contextlib import asynccontextmanager
from fastapi import FastAPI

from backend.items_views import router as items_router
from backend.users.views import router as users_router
from backend.core.models import Base, db_helper
from backend.core.config import settings
from backend.api_v1 import router as router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)
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
