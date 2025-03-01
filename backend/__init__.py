from backend.database import db_manager, get_db_session
from backend.config import database_url

from backend.models import User, Session, Tag


db_manager.init(database_url)
