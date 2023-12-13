from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    UserAPIView,
    UserAvatarAPIView,
    UserLoginAPIView,
    UserLogoutAPIView,
    UserProfileAPIView,
    UserRegisterationAPIView,
)
from posts.views.choice_fields import ActivityViewSet, EnsembleViewSet, PositionViewSet, LocationViewSet

app_name = 'users'

urlpatterns = [
    path('register/', UserRegisterationAPIView.as_view(), name='create-user'),
    path('login/', UserLoginAPIView.as_view(), name='login-user'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout-user'),
    path('', UserAPIView.as_view(), name='user-info'),
    path('profile/', UserProfileAPIView.as_view(), name='user-profile'),
    path('profile/avatar/', UserAvatarAPIView.as_view(), name='user-avatar'),

    path('activity/', ActivityViewSet.as_view(), name='activity_list'),
    path('ensemble/', EnsembleViewSet.as_view(), name='ensemble_list'),
    path('position/', PositionViewSet.as_view(), name='position_list'),
    path('location/', LocationViewSet.as_view(), name='location_list'),
]
