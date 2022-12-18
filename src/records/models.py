from datetime import datetime

from beanie import Document, Indexed, Link, before_event, Replace, Insert
from pydantic import Field

from categories.models import Category
from src.users.models import User
from tags.models import Tag
from templates.models import Template


class Record(Document):
    title: Indexed(str)
    data: dict | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    owner: Link[User]
    template: Link[Template] | None
    tags: list[Link[Tag]] | None
    categories: list[Link[Category]] | None

    def __repr__(self) -> str:
        return f"<Record {self.title}>"

    def __str__(self) -> str:
        return self.title

    def __hash__(self) -> int:
        return hash(self.title)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Record):
            return self.id == other.id
        return False

    @before_event([Replace, Insert])
    def update_updated_at(self):
        self.updated_at = datetime.utcnow()

    class Collection:
        name = "records"
