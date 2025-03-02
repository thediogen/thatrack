import uuid

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import select

from backend.database import Session_dp


class Base(AsyncAttrs, DeclarativeBase):

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + 's'


    @classmethod
    async def create(cls, session: Session_dp, **kwargs):
        instance = cls(**kwargs)

        session.add(instance)
        await session.commit()

        return instance

    @classmethod
    async def get(cls, session: Session_dp, field, value):
        stmt = select(cls).where(field == value)
        instance = await session.execute(stmt)
        instance = instance.scalar_one()

        return instance

    @classmethod
    async def all(cls, session: Session_dp):
        query = await session.execute(select(cls))
        result = query.scalars().all()

        return result
