from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from apis.tables import models, schemas
from database.database import get_db

router = APIRouter(prefix="/tables", tags=["tables"])


@router.get("/", response_model=list[schemas.TableResponse])
async def read_tables(db: AsyncSession = Depends(get_db)):
    """
    Retrieve all restaurant tables.
    """
    result = await db.execute(select(models.Table).order_by(models.Table.number))
    return result.scalars().all()

