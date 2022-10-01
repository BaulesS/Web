from django.urls import path 
from . import views


app_name= "main"

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('register/', views.signupPage, name="signup"),
	path('logout/', views.logoutUser, name="logout"),

    path('', views.IndexView.as_view(), name='index'),
    path('categories/', views.AnimeView.as_view(), name="animes"),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blogaddinfo/', views.BlogAddInfo.as_view(), name='blogaddinfo'),
    path('reviewaddinfo/', views.ReviewAddInfo.as_view(), name='reviewaddinfo'),
    path('review/', views.ReviewView.as_view(), name='review'),
    
]