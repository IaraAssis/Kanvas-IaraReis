from rest_framework import generics
from .serializers import CourseSerializer
from .models import Course
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.permissions import IsSuperUser
from rest_framework.response import Response
from rest_framework import status


class CreateCourseView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsSuperUser]

    # def perform_create(self, serializer):


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.select_related("instructor").all()
    serializer_class = CourseSerializer
    permission_classes = [IsSuperUser]
    authentication_classes = [JWTAuthentication]
    lookup_field = "course_id"

    # def perform_destroy(self, instance):
    #     instance.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
