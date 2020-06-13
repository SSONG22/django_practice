from django.urls import include,path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from rest_framework_jwt.views import refresh_jwt_token

from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('token', obtain_jwt_token),
    path('token/verify', verify_jwt_token),
    path('token/refresh', refresh_jwt_token),
]