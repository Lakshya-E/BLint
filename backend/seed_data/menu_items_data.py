import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
import asyncio
from apis.menu.models import MenuItem
from database.database import AsyncSessionLocal
from sqlalchemy.dialects.postgresql import insert


async def seed_menu(menu_items):
    async with AsyncSessionLocal() as session:
        for item_data in menu_items:
            stmt = insert(MenuItem).values(**item_data)
            stmt = stmt.on_conflict_do_update(
                index_elements=[MenuItem.name],
                set_=item_data
            )
            await session.execute(stmt)
        await session.commit()

if __name__ == "__main__":
    with open("seed_data/dev/menu_items.json", "r") as f:
        menu_items = json.load(f)
    asyncio.run(seed_menu(menu_items))
