from django.urls import path
from . import views
from rest_framework_simplejwt.views import token_obtain_pair

urlpatterns = [
    path("accounts/", views.CreateAccountView.as_view()),
    path("login/", token_obtain_pair),
]
