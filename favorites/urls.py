from django.urls import path
from .views import SavedBlogPostList, SavedBlogPostDetail

urlpatterns = [
    path("", SavedBlogPostList.as_view(), name="saved_blog_post_list"),
    path("<int:pk>/", SavedBlogPostDetail.as_view(), name="saved_blog_post_detail"),
]