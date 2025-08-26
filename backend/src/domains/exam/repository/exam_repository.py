from abc import ABC, abstractmethod
from typing import Any
from uuid import UUID

from ..entities import Exam


class ExamRepository(ABC):

    @abstractmethod
    def create(self, exam: Exam):
        pass

    @abstractmethod
    def list_all(self) -> list[Any]:
        pass

    @abstractmethod
    def get_by_id(self) -> Exam:
        pass

    @abstractmethod
    def save(self, exam: Exam) -> None:
        pass

    @abstractmethod
    def delete(self, id: UUID):
        pass
