# src/app/blog/urls.py

# Django and third parties modules
from django.urls import path

# Locals
from app.blog import views

# app name
app_name = "blog"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("about/", views.about_view, name="about"),
    path("blogs/<int:category_id>/", views.blogs_by_category_view, name="posts_by_category"),
    path('blogs/<slug:slug>/', views.blogs_by_slug_view, name='blogs_by_slug'),

    # Search endpoint
    path("blog/search/", views.search_view, name="search"),
]

