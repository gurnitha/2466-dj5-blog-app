# src/config/urls.py

# Django and third parties modules
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # user
    path("", include("app.user.urls", namespace="user")),
    
    # admin
    path("admin/", admin.site.urls),

    # blog
    path("", include("app.blog.urls", namespace="blog")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
