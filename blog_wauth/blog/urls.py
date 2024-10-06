from django.urls import path
from .import views

urlpatterns = [
    path('', views.home_view, name='blog-home'),
    path('login/', views.login_view, name = 'login'),
    path('register/', views.register_view, name = 'register'),
    path('new/', views.create_post_view, name = 'create_post'),
    path('post/<int:post_id>/', views.post_detail_view, name = 'post_detail'),
    
]


