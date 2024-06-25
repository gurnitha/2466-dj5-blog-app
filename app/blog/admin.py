# src/app/blog/admin.py

# Django and third parties modules
from django.contrib import admin


# Locals
from app.blog.models import Category, Blog, About, SocialLink


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured',)

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(About)
admin.site.register(SocialLink)