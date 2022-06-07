from django.shortcuts import render
# from django.http import HttpResponse

posts = [
    {
        "author": "CoreyMS",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "August 27, 2019"
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "August 28, 2019"
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    context = {
        'title': "About"
    }
    return render(request, 'blog/about.html', context=context)


def bootstrap(request):
    return render(request)