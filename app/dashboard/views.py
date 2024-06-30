# src/app/dashboard/views.py

# Django and third parties modules
from django.shortcuts import render

# Locals
from app.blog.models import Category, Blog

# Create your views here.

def dashboard_view(request):

	category_count = Category.objects.all().count()
	blog_count = Blog.objects.all().count()

	# Tesing
	# print(blog_count)

	data = {
		"category_count":category_count,
		"blog_count":blog_count
	}
	
	return render(request, "dashboard/dashboard.html", data)