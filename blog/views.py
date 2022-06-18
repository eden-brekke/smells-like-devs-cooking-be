from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import BlogPost
from .permissions import IsOwnerOrReadOnly
from .serializers import BlogPostSerializer


class BlogPostList(ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer