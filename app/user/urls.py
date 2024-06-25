# src/app/user/urls.py

# Django and third parties modules
from django.urls import path

# Locals
from app.user import views

# app name
app_name = "user"

urlpatterns = [
    path("user/register/", views.register_view, name="register"),
    path("user/login/", views.login_view, name="login"),
]