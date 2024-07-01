# src/app/dashboard/views.py

# Django and third parties modules
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify

# Locals
from app.blog.models import Category, Blog
from app.dashboard.forms import CategoryForm, BlogForm

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


def delete_category_view(request, pk):
	category = get_object_or_404(Category, pk=pk)
	category.delete()
	return redirect("dashboard:dashboard_category")


# ==================CRUD BLOGS=================


def dashboard_blog_view(request):

	blogs = Blog.objects.all()
	blog_count = Blog.objects.all().count()

	data = {
		'blogs': blogs,
		"blog_count":blog_count,
	}

	return render(request, "dashboard/blogs.html", data)


def add_blog_view(request):

	if request.method == 'POST':
		form = BlogForm(request.POST, request.FILES)
		if form.is_valid():
			blog = form.save(commit=False) # temporarily saving the form
			blog.author = request.user
			blog.save()
			title = form.cleaned_data['title']
			blog.slug = slugify(title) + '-'+str(blog.id)
			blog.save()
			return redirect("dashboard:add_blog")
		else:
			print('form is invalid')
			print(form.errors)

	else:
		form = BlogForm()

	data = {
		"form":form,
	}

	return render(request, "dashboard/add_blog.html", data)