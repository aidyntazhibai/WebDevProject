# blog/views.py

from rest_framework import generics, permissions, status
from .models import PostModel, Comment
from .serializers import PostModelSerializer, CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class PostList(generics.ListCreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

@api_view(['POST'])
def create_comment(request, pk):
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, post_id=pk)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
