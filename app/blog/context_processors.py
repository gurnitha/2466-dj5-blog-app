# src/app/blog/context_processors.py.py

# Locals
from app.blog.models import Category


def get_categories(request):
	categories = Category.objects.all()
	return dict(categories=categories)