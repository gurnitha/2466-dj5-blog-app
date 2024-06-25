# src/app/blog/views.py

# Django and third parties modules
from django.shortcuts import render

# Locals
from app.user.forms import RegistrationForm

# Create your views here.

def register_view(request):

	form = RegistrationForm()

	data = {
		"form":form
	}
	return render(request, "user/register.html", data)
