# src/app/dashboard/forms.py

# Django and third parties modules
from django import forms

# Locals
from app.blog.models import Category


class CategoryForm(forms.ModelForm):
	
    class Meta:
        model = Category
        fields = '__all__'