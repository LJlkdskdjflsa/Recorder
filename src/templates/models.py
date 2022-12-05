from datetime import datetime
from uuid import UUID, uuid4

from beanie import Document, Indexed, Link, before_event, Replace, Insert
from pydantic import Field

from src.users.models import User


class Template(Document):
    template_id: UUID = Field(default_factory=uuid4, unique=True)
    title: Indexed(str)
    description: str | None = None
    json_schema: dict | None = None
    ui_schema: dict | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    owner: Link[User]

    def __repr__(self) -> str:
        return f"<Template {self.title}>"

    def __str__(self) -> str:
        return self.title

    def __hash__(self) -> int:
        return hash(self.title)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Template):
            return self.template_id == other.template_id
        return False

    @before_event([Replace, Insert])
    def update_updated_at(self):
        self.updated_at = datetime.utcnow()

    class Collection:
        name = "templates"
