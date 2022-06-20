from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db import models
from blog.models import BlogPost


# Create your models here.
class SavedBlogPosts(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    blogPostID = models.ForeignKey(BlogPost, blank=True, null=True, on_delete=models.CASCADE)


