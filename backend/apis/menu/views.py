# api/menu/view.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from apis.menu import models, schemas
from database.database import get_db 

router = APIRouter(prefix="/menu/items", tags=["menu"])


@router.get("/", response_model=list[schemas.MenuItemResponse])
async def read_menu_items(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.MenuItem).order_by(models.MenuItem.id))
    return result.scalars().all()


@router.post("/", response_model=schemas.MenuItemResponse, status_code=201)
async def create_menu_item(item: schemas.MenuItemCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.MenuItem).filter_by(name=item.name))
    if result.scalars().first():
        raise HTTPException(status_code=400, detail="Item already exists")
        
    menu_item = models.MenuItem(**item.dict())
    db.add(menu_item)
    await db.commit()
    await db.refresh(menu_item)
    return menu_item


