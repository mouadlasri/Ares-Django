from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.


class PostListView(ListView):
    model = Post # retrieve all Posts through our Post model
    template_name = 'home/main.html'  # <app>/<model>_<viewtype>.html    viewtype is a 'list' in this case
    context_object_name = 'posts'
    ordering = ['-date_posted']  # order from newest to oldest
    
class PostDetailView(DetailView):
    model = Post
    # no need to specify the template_name because the template is already named the default (conventional way) ie:
    # <app>/<model>_<viewtype>.html   ie    home/post_detail.html
    slug_field = 'title'
