from django.urls import path, include
from rest_framework import routers

from . import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('posts2', views.PostViewSet)

urlpatterns = [
    path('simple/', views.simple),
    path('titles/', views.PostTitles.as_view()),
    path('posts/', views.Posts.as_view()),
    path('', include(router.urls))
]
