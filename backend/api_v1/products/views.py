from fastapi import APIRouter

from backend.api_v1.products import crud
from backend.api_v1.products.schemas import ProductCreate

router = APIRouter(tags=["products"])


@router.get("/")
async def get_products(session):
    return await crud.get_products(session=session)


@router.get("/{id}")
async def get_product(id: int, session):
    return await crud.get_product(session=session, product_id=id)


@router.post("/")
async def create_product(session, product_in: ProductCreate):
    return await crud.create_product(session=session, product_in=product_in)
