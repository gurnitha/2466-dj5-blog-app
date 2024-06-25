# src/app/blog/views.py

# Django and third parties modules
from django.shortcuts import render
from django.shortcuts import redirect

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

	return render(request, "user/login.html")
