# src/app/dashboard/urls.py

# Django and third parties modules
from django.urls import path

# Locals
from app.dashboard import views

# app name
app_name = "dashboard"

urlpatterns = [
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("dashboard/categories/", views.dashboard_category_view, name="dashboard_category"),
    path("dashboard/categories/add/", views.add_category_view, name="add_category"),
    path("dashboard/categories/edit/<int:pk>/", views.edit_category_view, name="edit_category"),
    path("dashboard/categories/delete/<int:pk>/", views.delete_category_view, name="delete_category"),
]

