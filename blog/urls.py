from django.contrib import admin
from django.urls import path
from blog.views import *

urlpatterns = [
    path('', home_page, name='Home Page'),
    path('post/<int:pk>/', blog_details, name='Full Blog')
]
