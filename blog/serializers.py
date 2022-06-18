from .models import BlogPost
from rest_framework import serializers 

class BlogPostSerializer(serializers.ModelSerializer):
  class Meta:
    fields = "__all__"
    model = BlogPost