from django.db import models


# Create your models here.

class Category(models.Model):
    blog_category = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.blog_category

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name='posts')
    
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=30)
    comment_body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.author} commented on '{self.post}'"