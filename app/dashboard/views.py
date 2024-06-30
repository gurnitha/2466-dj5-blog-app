# src/app/dashboard/views.py

# Django and third parties modules
from django.shortcuts import render

# Locals

# Create your views here.

def dashboard_view(request):
	
	return render(request, "dashboard/dashboard.html")