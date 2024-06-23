# src/app/blog/admin.py

# Django and third parties modules
from django.contrib import admin


# Locals
from app.blog.models import Category, Blog


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)