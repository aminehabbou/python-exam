from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from storage.relational import Base


class Message(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    object: Mapped[str] = mapped_column(String(200))
    created: Mapped[int] = mapped_column()
    model: Mapped[str] = mapped_column(String(200))


class choice(Base):
    index: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    finish_reason: Mapped[str] = mapped_column(String(500))
    message: Mapped[str] = mapped_column(String(1000))


class conversation_history(Base):
    role: Mapped[str] = mapped_column(String(100))
    content: Mapped[str] = mapped_column(String(1000))
