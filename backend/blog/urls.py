# blog/urls.py

from django.urls import path
from .views import PostList, PostDetail, create_comment

urlpatterns = [
    path('api/posts/', PostList.as_view(), name='post-list'),
    path('api/posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('api/posts/<int:pk>/comment/', create_comment, name='create-comment'),
]
