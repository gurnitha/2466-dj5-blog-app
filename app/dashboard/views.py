# src/app/dashboard/views.py

# Django and third parties modules
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Locals
from app.blog.models import Category, Blog
from app.dashboard.forms import CategoryForm

# Create your views here.

@login_required(login_url="user:login")
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



def dashboard_category_view(request):

	category_count = Category.objects.all().count()

	data = {
		"category_count":category_count,
	}

	return render(request, "dashboard/categories.html", data)


def add_category_view(request):

	if request.method == "POST":

		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("dashboard:dashboard_category")
	
	else:
		form = CategoryForm()

	data = {
		"form":form
	}
	
	return render(request, "dashboard/add_category.html", data)
