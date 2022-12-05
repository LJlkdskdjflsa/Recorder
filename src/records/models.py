from datetime import datetime
from uuid import UUID, uuid4

from beanie import Document, Indexed, Link, before_event, Replace, Insert
from pydantic import Field

from src.users.models import User


class Record(Document):
    record_id: UUID = Field(default_factory=uuid4, unique=True)
    title: Indexed(str)
    data: dict | None = None

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    owner: Link[User]

    def __repr__(self) -> str:
        return f"<Record {self.title}>"

    def __str__(self) -> str:
        return self.title

    def __hash__(self) -> int:
        return hash(self.title)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Record):
            return self.record_id == other.record_id
        return False

    @before_event([Replace, Insert])
    def update_updated_at(self):
        self.updated_at = datetime.utcnow()

    class Collection:
        name = "records"
