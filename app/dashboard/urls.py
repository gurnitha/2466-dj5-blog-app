# src/app/dashboard/urls.py

# Django and third parties modules
from django.urls import path

# Locals
from app.dashboard import views

# app name
app_name = "dashboard"

urlpatterns = [
    path("dashboard/", views.dashboard_view, name="dashboard"),

    # crud categories
    path("dashboard/categories/", views.dashboard_category_view, name="dashboard_category"),
    path("dashboard/categories/add/", views.add_category_view, name="add_category"),
    path("dashboard/categories/edit/<int:pk>/", views.edit_category_view, name="edit_category"),
    path("dashboard/categories/delete/<int:pk>/", views.delete_category_view, name="delete_category"),

    # crud blogs
    path("dashboard/blogs/", views.dashboard_blog_view, name="dashboard_blog"),
    path("dashboard/blogs/add/", views.add_blog_view, name="add_blog"),
    path("dashboard/blogs/edit/<int:pk>/", views.edit_blog_view, name="edit_blog"),
    path("dashboard/blogs/delete/<int:pk>/", views.delete_blog_view, name="delete_blog"),

    # users
    path("dashboard/users/", views.dashboard_user_view, name="dashboard_user"),
    path("dashboard/users/add/", views.add_user_view, name="add_user"),
    path("dashboard/users/edit/<int:pk>/", views.edit_user_view, name="edit_user"),
]

