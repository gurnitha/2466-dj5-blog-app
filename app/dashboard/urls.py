# src/app/dashboard/urls.py

# Django and third parties modules
from django.urls import path

# Locals
from app.dashboard import views

# app name
app_name = "dashboard"

urlpatterns = [
    path("dashboard/", views.dashboard_view, name="dashboard"),
]

