from uuid import UUID


class Course:
    """
    Couse Entity
    """

    def __init__(self, id: UUID, name: str, university: str, description: str):
        self.id = id
        self.name = name
        self.university = university
        self.description = description
