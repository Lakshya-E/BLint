# api/router.py

from fastapi import APIRouter
from .menu.views import router as menu_router
from .tables.views import router as tables_router
from database.views import router as database_router

api_router = APIRouter()
api_router.include_router(menu_router)
api_router.include_router(database_router)
api_router.include_router(tables_router)
