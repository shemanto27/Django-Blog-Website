from django.shortcuts import render
from blog.models import *

# Create your views here.
def home_page(request):
    posts = Post.objects.all().order_by("-created_on")
    recent_posts = Post.objects.all().order_by("-created_on")[:4]
    context = {
        'posts' : posts,
        'title' : "Shemanto's Blog",
        'recent_posts' : recent_posts,
    }
    return render(request, 'home.html', context)

def blog_details(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        'post' : post,
        'comments' : comments,
        'title' : post.title,
    }
    return render(request,'blog_details.html', context)
