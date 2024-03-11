from rest_framework import generics
from .serializers import ContentSerializer
from accounts.permissions import IsSuperUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import StudentPermission
from courses.models import Course
from contents.models import Content
from rest_framework.exceptions import NotFound
from rest_framework import permissions


class CreateContentView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUser]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "course_id"

    def perform_create(self, serializer):
        course = Course.objects.filter(pk=self.kwargs["course_id"]).first()
        if not course:
            raise NotFound({"detail": "course not found."})
        serializer.save(course=course)


class ContentDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [StudentPermission]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "content_id"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Content.objects.all()
        return Content.objects.filter(
            course__contents=self.kwargs[self.lookup_url_kwarg]
        )

    def get_object(self):
        if permissions.SAFE_METHODS:
            course = Course.objects.filter(
                pk=self.kwargs["course_id"],
            )
            contente = Content.objects.filter(
                pk=self.kwargs["content_id"],
            )
            if not contente:
                raise NotFound({"detail": "content not found."})
            if not course:
                raise NotFound({"detail": "course not found."})
        return super().get_object()
