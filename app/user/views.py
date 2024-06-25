# src/app/blog/views.py

# Django and third parties modules
from django.shortcuts import render

# Create your views here.

def register_view(request):
	return render(request, "user/register.html")
