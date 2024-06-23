# src/app/blog/views.py

# Django and third parties modules
from django.shortcuts import render

# Locals
from app.blog.models import Category, Blog

# Create your views here.

def home_view(request):

	# Select semua object dari tabel Category
	categories = Category.objects.all()

	# Select featured object dari Blog
	featured_posts = Blog.objects.filter(is_featured=True)

	# Select semua blogs yang bukan featured dengan status published
	posts = Blog.objects.filter(is_featured=False, status="Published")

	# Print objects untuk testing
	# print(posts)

	data = {
		"categories":categories,
		"featured_posts":featured_posts,
		"posts":posts
	}

	return render(request, "blog/index.html", data)