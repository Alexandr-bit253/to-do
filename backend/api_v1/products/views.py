from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.api_v1.products import crud
from backend.api_v1.products.dependencies import product_by_id
from backend.api_v1.products.schemas import ProductCreate, Product
from backend.core.models import db_helper

router = APIRouter(tags=["Products"])


@router.get("/", response_model=list[Product])
async def get_products(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_products(session=session)


@router.post("/", response_model=Product)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_product(session=session, product_in=product_in)


@router.get("/{id}/", response_model=Product)
async def get_product(
    product: Product = Depends(product_by_id),
):
    return product


@router.put("/{id}/")
async def update_product():
    pass
