# src/app/blog/views.py

# Django and third parties modules
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q

# Locals
from app.blog.models import Category, Blog, About, Comment

# Create your views here.

def home_view(request):
	
	# Select featured object dari Blog
	featured_posts = Blog.objects.filter(is_featured=True)

	# # Select semua blogs yang bukan featured dengan status published
	posts = Blog.objects.filter(is_featured=False, status="Published")

	# # Print objects untuk testing
	# # print(posts)

	data = {
		"featured_posts":featured_posts,
		"posts":posts
	}

	return render(request, "blog/index.html", data)



def blogs_by_category_view(request, category_id):
    
    # Fetch the blogs that belongs to a category identified by its category_id
    blogs_by_category = Blog.objects.filter(status='Published', category=category_id)

    # Gunakan try/except untuk tidak memperlihatkan warning LAMAN TIDAK DITEMUI bila category tidak ada
    try:
        category = Category.objects.get(pk=category_id)
    except:
        # redirect the user to homepage
        return redirect('blog:home')

    # # Use get_object_or_404 when you want to show 404 error page if the category does not exist
    # category = get_object_or_404(Category, pk=category_id)

    data = {
        "blogs_by_category": blogs_by_category,
        "category":category,
    }

    return render(request, 'blog/blogs_by_category.html', data)


def blogs_by_slug_view(request, slug):
    
    single_blog = get_object_or_404(Blog, slug=slug, status="Published")

    # Comments
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()

    # testing
    # print("comment ==>", comments )

    data = {
        "single_blog":single_blog,
        "comments": comments,
        "comment_count":comment_count,
    }

    return render(request, 'blog/blogs_by_slug.html', data)


# src/app/blog/views.py
def about_view(request):

    about = About.objects.all()

    data = {
        "about":about
    }

    return render(request, 'blog/about.html', data)


def search_view(request):

    keyword = request.GET.get('keyword')
    
    # # Testing
    # print('this keyword', keyword)
    
    blogs = Blog.objects.filter(
        Q(title__icontains=keyword) | 
        Q(short_description__icontains=keyword) | 
        Q(blog_body__icontains=keyword), 
        status='Published')
  
    # Testing
    # print(blogs)

    data = {
        'blogs': blogs,
        'keyword': keyword,
    }

    return render(request, 'blog/search.html', data)