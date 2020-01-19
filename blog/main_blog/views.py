from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'main_blog/home.html', context)


def about(request):
    return render(request, 'main_blog/about.html', {'title': 'About'})
