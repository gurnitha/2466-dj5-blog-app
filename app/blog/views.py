# src/app/blog/views.py

# Django and third parties modules
from django.shortcuts import render

# Locals
from app.blog.models import Category

# Create your views here.

def home_view(request):

	# Select semua object dari tabel Category
	categories = Category.objects.all()
	
	# Print objects untuk testing
	print(categories)

	return render(request, "blog/index.html")