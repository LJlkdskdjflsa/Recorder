from datetime import datetime

from beanie import Document, Indexed, Link, before_event, Replace, Insert
from pydantic import Field

from users.models import User


class Category(Document):
    title: Indexed(str)
    description: str | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    owner: Link[User]

    def __repr__(self) -> str:
        return f"<Category {self.title}>"

    def __str__(self) -> str:
        return self.title

    def __hash__(self) -> int:
        return hash(self.title)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Category):
            return self.id == other.id
        return False

    @before_event([Replace, Insert])
    def update_updated_at(self):
        self.updated_at = datetime.utcnow()

    class Collection:
        name = "categories"
