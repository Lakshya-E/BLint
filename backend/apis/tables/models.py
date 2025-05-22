from sqlalchemy import Column, Integer, String
from database.database import Base

class Table(Base):
    __tablename__ = "restaurant_tables"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, unique=True, index=True)
    seats = Column(Integer)
    status = Column(String, default="available")  # e.g. "available", "occupied"
