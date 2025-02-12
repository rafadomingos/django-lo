from django.shortcuts import render
from django.http import HttpResponse, Http404

from . import data

def index(request):
    context = {
        'title': 'Blog Page',
        'posts': data.posts
    }

    return render(
        request, 
        'blog/index.html', 
        context    
    )


def post(request: HttpResponse, post_id:int):
    
    found_post = None

    for post in data.posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post not found')
    
    context = {
        'title': 'Blog Page',
        'post': found_post
    }

    return render(
        request, 
        'blog/post.html', 
        context    
    )