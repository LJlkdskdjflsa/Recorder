from datetime import datetime
from string import Template

from beanie import Document, Indexed, Link, before_event, Replace, Insert
from pydantic import Field

from categories.models import Category
from src.users.models import User
from tags.models import Tag


class Template(Document):
    title: Indexed(str)
    description: str | None
    json_schema: dict | None
    ui_schema: dict | None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    owner: Link[User]
    tags: list[Link[Tag]] | None
    categories: list[Link[Category]] | None

    def __repr__(self) -> str:
        return f"<Template {self.title}>"

    def __str__(self) -> str:
        return self.title

    def __hash__(self) -> int:
        return hash(self.title)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Template):
            return self.id == other.id
        return False

    @before_event([Replace, Insert])
    def update_updated_at(self):
        self.updated_at = datetime.utcnow()

    class Collection:
        name = "templates"
