from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import SavedBlogPosts
from blog.permissions import IsOwnerOrReadOnly
from .serializers import SavedBlogPostSerializer


# Create your views here.
class SavedBlogPostList(ListCreateAPIView):
    queryset = SavedBlogPosts.objects.all()
    serializer_class = SavedBlogPostSerializer


class SavedBlogPostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = SavedBlogPosts.objects.all()
    serializer_class = SavedBlogPostSerializer
