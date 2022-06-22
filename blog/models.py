from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.
class BlogPost(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    recipe_ingredients = models.JSONField(default=list, null=True)
    recipe_directions = models.JSONField(default=list, null=True)
    recipe_images = models.URLField(max_length=2000, null=True)  # CHECK, what will these be stored as?
    title = models.CharField(max_length=64, null=True)
    difficulty = models.IntegerField(null=True)
    recipe_intro = models.TextField(null=True)
    prep_time = models.IntegerField(null=True)
    cook_time = models.IntegerField(null=True)
    meal_type = models.CharField(max_length=64, null=True)


    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self): 
        return self.title
    
    def get_absolute_url(self): 
        return reverse("blog_post_detail", args=[str(self.id)])

    