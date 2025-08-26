from uuid import UUID


class Subject:
    """
    Subject Entity
    """

    def __init__(
        self,
        id: UUID,
        name: str,
        code: str,
        course_id: int,
        semester: str,
        credit_hour: str,
    ):
        self.id = id
        self.name = name
        self.code = code
        self.course_id = course_id
        self.semester = semester
        self.credit_hour = credit_hour
