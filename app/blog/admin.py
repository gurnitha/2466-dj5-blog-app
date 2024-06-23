# src/app/blog/admin.py

# Django and third parties modules
from django.contrib import admin


# Locals
from app.blog.models import Category


# Register your models here.

admin.site.register(Category)