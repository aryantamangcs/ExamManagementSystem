from datetime import date as dt
from datetime import time
from typing import Optional
from uuid import UUID


class Routine:
    """
    Routine Entity
    """

    def __init__(
        self,
        id: UUID,
        date: dt,
        start_time: time,
        end_time: time,
        teacher: str,
        subject_id: Optional[UUID] = None,
        name: Optional[str] = None,
    ):
        self.id = id
        self.subject_id = subject_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.teacher = teacher
        self.name = name

    # business rules

    def add_name(self, name: str):
        """
        Adds name to the routine
        Raises :
            Exception : If subject_id is not None you cannot add name
        """
        if self.subject_id:
            raise Exception("Cannot add name when subject is selected.")
        self.name = name
