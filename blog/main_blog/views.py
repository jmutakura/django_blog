from django.shortcuts import render


posts = [
    {
        'author': 'Jonathan',
        'title': 'Blog post 1',
        'content': 'First content posted',
        'date': 'January 18 2020'
    },
{
        'author': 'James Loo',
        'title': 'Blog post 2',
        'content': 'Second content posted',
        'date': 'January 28 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'main_blog/home.html', context)


def about(request):
    return render(request, 'main_blog/about.html')
