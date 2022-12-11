from beanie import Document, Indexed


class Tag(Document):
    title: Indexed(str, unique=True)

    def __repr__(self) -> str:
        return f"<Tag {self.title}>"

    def __str__(self) -> str:
        return self.title

    def __hash__(self) -> int:
        return hash(self.title)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Tag):
            return self.id == other.id
        return False

    class Collection:
        name = "tags"
