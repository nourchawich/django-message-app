from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name='list'),
    path('create/', views.posts_create, name='create'),
]

# Todo (Mentee): After creating the campaigns app
#  1. Create urls.py where you define paths for list and create campaigns views
