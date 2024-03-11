from rest_framework import permissions
from accounts.models import Account


class StudentPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Account):
        if (
            request.method in permissions.SAFE_METHODS
            and request.user in obj.course.students.all()
        ):
            return True
        return request.user.is_authenticated and request.user.is_superuser
