# src/app/blog/urls.py

# Django and third parties modules
from django.urls import path

# Locals
from app.blog import views

app_name = "blog"
urlpatterns = [
    path("", views.home_view, name="home"),
]

