# src/app/dashboard/views.py

# Django and third parties modules
from django.shortcuts import render, redirect, get_object_or_404
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

	
def edit_category_view(request, pk):

	category = get_object_or_404(Category, pk=pk)

	if request.method == 'POST':
		form = CategoryForm(request.POST, instance=category)
		if form.is_valid():
			form.save()
			return redirect("dashboard:dashboard_category")

	else:
		form = CategoryForm(instance=category)

	data = {
		'category': category,
		'form': form,
	}

	return render(request, "dashboard/edit_category.html", data)
