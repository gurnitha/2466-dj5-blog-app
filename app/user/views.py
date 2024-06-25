# src/app/blog/views.py

# Django and third parties modules
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth 

# Locals
from app.user.forms import RegistrationForm

# Create your views here.

def register_view(request):

	"""RegistrationForm ini akan dirender
	saat user mengklik tombol register"""
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("user:register")

	else:
		"""RegistrationForm ini akan dirender saat
		user mengklik menu register"""
		form = RegistrationForm()

	data = {
		"form":form
	}

	return render(request, "user/register.html", data)


def login_view(request):

	"""AuthenticationForm ini akan dirender
	saat user mengklik TOMBOL login"""
	if request.method == "POST":
		form = AuthenticationForm(request, request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = auth.authenticate(username=username, password=password)
			if user is not None:
				auth.login(request, user)
			return redirect("blog:home")

	else:
		"""AuthenticationForm ini akan dirender saat
		user mengklik MENU login"""
		form = AuthenticationForm()

	data = {
		"form":form
	}
	
	return render(request, "user/login.html", data)
