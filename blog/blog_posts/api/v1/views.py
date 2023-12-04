from rest_framework import generics, status
from rest_framework.generics import UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer, UserSerializer, PostUpdateSerializer
from ...domain.services.usecases import AuthorRegisterUseCase
from ...models import Post, Author

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AuthorRegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        username = request.data.get('username')
        bio = request.data.get('bio')
        profile_pic = request.data.get('profile_pic')

        author_register_usecase = AuthorRegisterUseCase()
        author_entity = author_register_usecase.execute(email, password, username, bio, profile_pic)

        response_data = {
            'email': author_entity.email,
            'username': author_entity.username,
            'bio': author_entity.bio,
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

# class PostDeleteView(DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostUpdateView(UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostUpdateSerializer
#
#
# class UserListAPIView(APIView):
#     def get(self, request):
#         authors = Author.objects.all()
#         serializer = UserSerializer(authors, many=True)
#         return Response(serializer.data)
#
#
# class BlogListAPIView(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = (IsAuthenticated,)
