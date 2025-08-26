from tortoise import fields
from tortoise.models import Model


class CourseModel(Model):

    id = fields.UUIDField(primary_key=True)
    name = fields.CharField(max_length=50)
    university = fields.CharField(max_length=50)
    description = fields.TextField()

    def __repr__(self):
        return f"{self.name}"


class SubjectModel(Model):

    id = fields.UUIDField(primary_key=True)
    name = fields.CharField(max_length=50)
    code = fields.CharField(max_length=50)
    course_id = fields.ForeignKeyField(
        model_name="CourseModel", on_delete=fields.CASCADE
    )
    semester = fields.CharField(max_length=50)
    credit_hour = fields.CharField(max_length=50)

    def __repr__(self):
        return f"{self.name}"
