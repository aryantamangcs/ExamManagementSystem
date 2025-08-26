from tortoise import fields
from tortoise.models import Model

from domains.exam.entities import ExamStatusEnum

from ..course.models import CourseModel, SubjectModel


class ExamModel(Model):

    __tablename__ = "exams"

    id = fields.UUIDField(primary_key=True)
    name = fields.CharField(max_length=50)
    exam_type = fields.CharField(max_length=50)
    start_date = fields.DateField()
    end_date = fields.DateField()
    course_id = fields.ForeignKeyField(
        model_name="CourseModel", on_delete=fields.CASCADE
    )
    semester = fields.CharField(max_length=50)
    routines = fields.ManyToManyField(
        model_name="RoutineModel", related_name="exam_routine"
    )
    status = fields.CharEnumField(enum_type=ExamStatusEnum)

    def __repr__(self):
        return f"{self.name}__{self.exam_type}"


class RoutineModel(Model):

    __tablename__ = "routines"

    id = fields.UUIDField(primary_key=True)
    subject_id = fields.ForeignKeyField(model_name="SubjectModel")
    date = fields.DateField()
    start_time = fields.TimeField()
    end_time = fields.TimeField()
    teacher = fields.CharField(max_length=50)
    name = fields.CharField(null=True)

    def __repr__(self):
        return f"{self.teacher}__{self.date}"
