from uuid import UUID
from decimal import Decimal
from pydantic import BaseModel
from .enums import CategoryEnum, SubCategoryEnum, CuisineEnum

class MenuItemCreate(BaseModel):
    name: str
    description: str
    category: CategoryEnum
    sub_category: SubCategoryEnum
    cuisine: CuisineEnum
    price: Decimal
    image_url: str | None = None

class MenuItemResponse(MenuItemCreate):
    id: UUID

    class Config:
        orm_mode = True
