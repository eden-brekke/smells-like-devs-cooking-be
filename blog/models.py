from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class BlogPost(models.Model):
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
