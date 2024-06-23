# src/app/blog/views.py

# Django and third parties modules
from django.shortcuts import render
from django.http import HttpResponse

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


def blogs_by_category_view(request, category_id):
    
    # Fetch the blogs that belongs to a category identified by its category_id
    blogs_by_category = Blog.objects.filter(status='Published', category=category_id)

    # Testing
    # return HttpResponse(blogs_by_category)

    data = {
        'blogs_by_category': blogs_by_category,
    }

    return render(request, 'blog/blogs_by_category.html', data)