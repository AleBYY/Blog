from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views

urlpatterns = [
    path('api/v1/post-list/<int:pk>/', views.BlogListAPIView.as_view()),
    path('api/v1/users-list', views.UserListAPIView.as_view()),
    path('api/v1/update/<int:pk>/', views.PostUpdateView.as_view()),
    path('api/v1/delete/<int:pk>/', views.PostDeleteView.as_view()),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
