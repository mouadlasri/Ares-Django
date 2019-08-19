from django.contrib import admin
from django.urls import path, include
from . import views
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name="main-home"),
    path('post/<slug>/', PostDetailView.as_view(), name="post-detail")
]
