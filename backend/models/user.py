from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from backend.models.base import Base
from backend.database import Session_dp


class User(Base):
    name: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()

    active: Mapped[bool] = mapped_column()

    tags = relationship('Tag')
    sessions = relationship('Session', back_populates='user')

    telegram_id: Mapped[str] = mapped_column(nullable=True, index=True)


    @classmethod
    async def get_active(cls, session: Session_dp):
        active_user = await User.get(session=session, field=User.active, value=True)

        return active_user

