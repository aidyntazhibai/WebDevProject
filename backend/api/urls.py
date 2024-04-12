from django.urls import path
from .views import *



urlpatterns = [
  path("category/<category>/", blog_category, name="blog_category"),
  path("", blog_index, name="blog_index"),
  path("post/<int:pk>/", blog_detail, name="blog_detail"),
]