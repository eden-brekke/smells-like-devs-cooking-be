from .models import SavedBlogPosts
from rest_framework import serializers


class SavedBlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = SavedBlogPosts
