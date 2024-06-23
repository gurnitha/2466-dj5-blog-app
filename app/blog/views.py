# src/app/blog/views.py

# Django and third parties modules
from django.shortcuts import render

# Create your views here.

def home_view(request):
	return render(request, "blog/index.html")
