from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)
from . import views

appname = 'accounts'
urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("logout/", TokenBlacklistView.as_view(), name='token_blacklist'),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", views.AccountAPIView.as_view(), name="register"),
    path("<str:username>/", views.AccountDetailAPIView.as_view(), name="profile"),
]