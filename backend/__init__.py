import asyncio

from backend.database import db_manager, get_db_session
from backend.config import database_url
from backend.models import User, Session, Tag


db_manager.init(database_url)


async def get_active_user() -> User:
    async with db_manager.session() as session:
        active_user = await User.get_active(session=session)

        return active_user
    

try:
    active_user = asyncio.run(get_active_user())
except Exception as er:
    print(er)
