"""
URL configuration for MyBlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views
from .views import (
    home, 
    about, 
    register, 
    custom_logout,  # ← ДОБАВЬТЕ ЭТОТ ИМПОРТ
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView
)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(
    template_name='blog/login.html',
    redirect_authenticated_user=True  # Если уже вошел → перенаправить
), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]