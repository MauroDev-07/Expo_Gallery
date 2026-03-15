from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .view import UserViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

