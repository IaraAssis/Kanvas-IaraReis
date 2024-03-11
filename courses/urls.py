from django.urls import path
from . import views
# from contents import views as content_views

urlpatterns = [
    path("courses/", views.CreateCourseView.as_view()),
    path("courses/<uuid:course_id>/", views.CourseDetailView.as_view()),
    # path(
    #     "courses/<uuid:course_id>/contents/",
    #     content_views.CreateContentView.as_view()),
        ]
