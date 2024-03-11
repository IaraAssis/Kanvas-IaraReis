from django.urls import path
from . import views


urlpatterns = [
    path("courses/<course_id>/contents/", views.CreateContentView.as_view()),
    path(
        "courses/<course_id>/contents/<content_id>/",
        views.ContentDetailView.as_view()
    ),
]
