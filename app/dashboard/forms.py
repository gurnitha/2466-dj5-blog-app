# src/app/dashboard/forms.py

# Django and third parties modules
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Locals
from app.blog.models import Category, Blog


class CategoryForm(forms.ModelForm):
	
	class Meta:
		model = Category
		fields = '__all__'


class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = (
				'title', 'category', 'featured_image', 
				'short_description', 'blog_body', 'status', 
				'is_featured')


class AddUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = (
			'username', 'email', 'first_name', 
			'last_name', 'is_active', 'is_staff', 
			'is_superuser', 'groups', 'user_permissions')


class EditUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = (
			'username', 'email', 'first_name', 
			'last_name', 'is_active', 'is_staff', 
			'is_superuser', 'groups', 'user_permissions')