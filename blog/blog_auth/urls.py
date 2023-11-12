from django.urls import path
from .views import Register, Login, ProfileEditView, ProfileDetailView
from . import views

urlpatterns = [
    path('login/', Login.as_view(), name='login_page'),
    path('register/', Register.as_view(), name='registration'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile_edit'),
    path('logout/', views.logout_page, name='logout_page'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('subscribe/<int:pk>/', views.subscribe, name='subscribe'),
    path('unsubscribe/<int:pk>/', views.unsubscribe, name='unsubscribe'),
    path('following/<int:pk>/', views.FollowingListView.as_view(), name='following_list'),
    path('followers/<int:pk>/', views.FollowersListView.as_view(), name='followers_list'),




]
