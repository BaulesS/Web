"""AnimeWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name= "main"

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(('main.urls', 'main' ), namespace='main')),
]

if settings.DEBUG: 
   urlpatterns += static(settings.STATIC_URL, documment_root = settings.STATIC_ROOT) 

#path('', views.IndexView.as_view(), name="index"),
    # path('review/', views.ReviewView.as_view(), name="review"),
    # path('review/<slug:slug>', views.ReviewDetailView.as_view(), name="reviews"),
    # path('blog/', views.BlogView.as_view(), name= "blog"),
    # path('blog/<slug:slug>', views.BlogDetailView.as_view(), name= "blogs"),
