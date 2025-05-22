import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, Enum, Numeric
from database.database import Base
from .enums import CategoryEnum, SubCategoryEnum, CuisineEnum

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    category = Column(Enum(CategoryEnum, name="categoryenum"), nullable=False)
    sub_category = Column(Enum(SubCategoryEnum, name="subcategoryenum"), nullable=True)
    cuisine = Column(Enum(CuisineEnum, name="cuisineenum"), nullable=True)
    price = Column(Numeric(10, 2))
    image_url = Column(String)
