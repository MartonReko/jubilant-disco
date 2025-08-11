from sqlmodel import Field, SQLModel


class BaseTable(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
