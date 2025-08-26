from datetime import date
from enum import Enum
from uuid import UUID


class ExamStatusEnum(str, Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    CLOSED = "closed"


class Exam:
    """
    Exam Entity
    """

    def __init__(
        self,
        id: UUID,
        name: str,
        exam_type: str,
        start_date: date,
        end_date: date,
        course_id: int,
        semester: str,
        routine: list[UUID],
        status: ExamStatusEnum = ExamStatusEnum.DRAFT,
    ):
        self.id = id
        self.name = name
        self.exam_type = exam_type
        self.start_date = start_date
        self.end_date = end_date
        self.course_id = course_id
        self.semester = semester
        self.routines: list[UUID] = routine
        self.status = status

    # business rules
    def publish(self):
        """
        Change exam status to published

        Raises:
            Exception: If the exam is not in DRAFT status

        """
        if self.status != ExamStatusEnum.DRAFT:
            raise Exception("Only draft status can be published.")
        self.status = ExamStatusEnum.PUBLISHED

    def close(self):
        """
        Close the exam status

        Raises:
            Exception : If the exam is not published
        """
        if self.status != ExamStatusEnum.PUBLISHED:
            raise Exception("Only published status can be closed.")
        self.status = ExamStatusEnum.CLOSED

    def add_routine(self, routine_id: int):
        """
        Adds the routine to the exam
        Raises :
            Exception : If routine is already added
        """
        if routine_id in self.routines:
            raise Exception("Already registered")
        self.routines.append(routine_id)
