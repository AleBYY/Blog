from rest_framework import generics
from rest_framework.generics import UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer, UserSerializer, PostUpdateSerializer
from ...models import Post, Author


class PostDeleteView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostUpdateView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer


class UserListAPIView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = UserSerializer(authors, many=True)
        return Response(serializer.data)


class BlogListAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
