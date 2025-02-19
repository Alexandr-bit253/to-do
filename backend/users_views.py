from fastapi import APIRouter
from pydantic import BaseModel, EmailStr


class CreateUser(BaseModel):
    email: EmailStr
    name: str


router = APIRouter(prefix="/users")


@router.post("/")
async def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email
    }
    