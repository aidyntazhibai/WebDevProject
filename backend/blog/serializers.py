from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PostModel, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PostModelSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    
    class Meta:
        model = PostModel
        fields = ['id', 'title', 'content', 'author', 'date_created', 'comment_count']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=PostModel.objects.all())
    
    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'content']
