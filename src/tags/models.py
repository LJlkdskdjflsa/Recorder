from uuid import UUID, uuid4

from beanie import Document, Indexed
from pydantic import Field


class Tag(Document):
    tag_id: UUID = Field(default_factory=uuid4, unique=True)
    title: Indexed(str, unique=True)

    def __repr__(self) -> str:
        return f"<Tag {self.title}>"

    def __str__(self) -> str:
        return self.title

    def __hash__(self) -> int:
        return hash(self.title)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Tag):
            return self.tag_id == other.tag_id
        return False

    class Collection:
        name = "tags"
