from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import UserViewSet, getPerfilView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, )

router_user = DefaultRouter()

router_user.register(
    prefix='users',
    viewset=UserViewSet,
    basename='users'
)

urlpatterns = [
    path('auth/me/', getPerfilView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router_user.urls
