from rest_framework import serializers
from blog_comments.models import Comment
from blog_posts.models import Author, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['name', 'description']


class PostDeleteSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
