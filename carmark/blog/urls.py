from django.urls import path
from . import views


app_name = 'blog'


urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<slug:slug>/', views.detail, name='car_detail'),
    path('like/<slug:slug>/', views.car_like, name='like'),
    path('dislike/<slug:slug>/', views.car_dislike, name='dislike'),
]
