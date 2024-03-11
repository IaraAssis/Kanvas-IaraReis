from rest_framework import serializers
from .models import Course
from accounts.models import Account
from contents.serializers import ContentSerializer
from students_courses.serializers import StudentCourseSerializer


class CourseSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)
    students_courses = StudentCourseSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
        ]


class UpdateCourseSerializer(serializers.ModelSerializer):
    students_courses = StudentCourseSerializer(many=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
        ]
        extra_kwargs = {"name": {"read_only": True}}

    def update(self, instance, validated_data):
        students = []
        not_students = []
        for student in validated_data["students_courses"]:
            course = student["student"]
            found_student = Account.objects.filter(email=course["email"]).first()
            if found_student:
                students.append(found_student)
            else:
                not_students.append(course["student"])
        if not_students:
            raise serializers.ValidationError(
                {"detail": f"No active accounts was found: {', '.join(not_students)}."}
            )
        instance.students.add(*students)
        return instance
