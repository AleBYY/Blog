from django.urls import path
from .views import BlogListView, BlogDetailView, PostCreateView
from . import views

urlpatterns = [
    path('', BlogListView.as_view(), name='posts_list'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/add/', PostCreateView.as_view(), name='post_add'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
    path('post/<int:pk>/dislike/', views.dislike_post, name='dislike_post'),
    path('post/<int:post_id>/reacted-users/', views.UserReactionListView.as_view(), name='reacted_users'),
    path('search/', views.SearchResultsView.as_view(), name='search_posts'),

]
