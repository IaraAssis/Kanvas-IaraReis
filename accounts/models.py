from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        max_length=150,
        unique=True,
        error_messages={'unique': 'A user with that username already exists.'}
    )
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=100, unique=True)
    is_superuser = models.BooleanField(default=False)
    my_courses = models.ManyToManyField(
        "courses.Course",
        through="students_courses.StudentCourse",
        related_name="students",
    )
