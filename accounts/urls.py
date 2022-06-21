from django.urls import path
from .views import UserDetailAPI,RegisterUserAPIView
urlpatterns = [
  #is the get-details going to show details for the currently logged in user? 
  path("get-details",UserDetailAPI.as_view()),
  path('register',RegisterUserAPIView.as_view()),
]