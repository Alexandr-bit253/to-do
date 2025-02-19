from typing import Dict, Any
from users.schemas import CreateUser


def create_user(user_in: CreateUser) -> Dict[str, Any]:
    user = user_in.model_dump()
    return {
        "success": True,
        "user": user,
    }
