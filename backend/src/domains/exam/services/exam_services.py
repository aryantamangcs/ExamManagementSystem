from uuid import UUID

from ..entities import Routine


class ExamServices:

    @staticmethod
    def schedule_routine(routine: Routine, existing_routines: list[UUID]):
        if routine.id in existing_routines:
            raise Exception(f"This course has been already scheduled for exam.")
        if routine.start_time >= routine.end_time:
            raise Exception(f"Start time cannot elapse end_time")
        existing_routines.append(routine.id)
