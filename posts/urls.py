from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name='list'),
    path('create/', views.posts_create, name='create'),
]

