from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import (
    UserRegisterationAPIView,
    UserLoginAPIView,
    UserLogoutAPIView,
    UserAPIView,
    UserAvatarAPIView,
    UserProfileAPIView
)

app_name = "users"

urlpatterns = [
    path("register/", UserRegisterationAPIView.as_view(), name="create-user"),
    path("login/", UserLoginAPIView.as_view(), name="login-user"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("logout/", UserLogoutAPIView.as_view(), name="logout-user"),
    path("", UserAPIView.as_view(), name="user-info"),
    path("profile/", UserProfileAPIView.as_view(), name="user-profile"),
    path("profile/avatar/", UserAvatarAPIView.as_view(), name="user-avatar"),
]
