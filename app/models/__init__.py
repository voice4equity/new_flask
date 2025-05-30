# app/models/example.py   (create more files in app/models/ as needed)
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app import db   # db is the SQLAlchemy() instance from Flask-SQLAlchemy

class Example(db.Model):
    __tablename__ = "examples"           # explicit table name (recommended)

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64), nullable=False)

    def __repr__(self) -> str:
        return f"<Example id={self.id} name={self.name!r}>"

