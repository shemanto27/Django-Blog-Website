from django.shortcuts import render
from blog.models import *
from django.core.paginator import Paginator

# Create your views here.
# -----------Home Page View-------------------
def home_page(request):
    posts = Post.objects.all().order_by("-created_on")
    recent_posts = posts[:4]
    context = {
        'posts' : posts,
        'title' : "Shemanto's Blog",
        'recent_posts' : recent_posts,
    }
    return render(request, 'home.html', context)


# -----------All Blogs View-------------------
def all_blogs(request):
    posts = Post.objects.all().order_by("-created_on")
    
    paginated = Paginator(posts,3)
    page_number = request.GET.get('page')
    page = paginated.get_page(page_number)
    
    context = {
        'posts' : posts,
        'title' : "Read Blogs",
        'page' : page,
    }
    return render(request, 'all_blogs.html', context)

# -----------Full Blog View-------------------
def blog_details(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        'post' : post,
        'comments' : comments,
        'title' : post.title,
    }
    return render(request,'blog_details.html', context)
