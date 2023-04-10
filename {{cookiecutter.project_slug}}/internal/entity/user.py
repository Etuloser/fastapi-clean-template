from typing import Optional

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
