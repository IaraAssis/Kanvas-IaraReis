from .models import StudentCourse
from rest_framework import serializers


class StudentCourseSerializer(serializers.ModelSerializer):
    stundent_username = serializers.CharField(
        read_only=True,
        source="student.username"
    )
    student_email = serializers.CharField(source="student.email")

    class Meta:
        model: StudentCourse
        fields = ["id", "status", "student_id"]
