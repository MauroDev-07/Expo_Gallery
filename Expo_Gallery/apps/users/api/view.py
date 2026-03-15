from rest_framework import viewsets, permissions
from rest_framework.response import Response
from ..models import User
from .serializers import UserSerializer

class UserViewSet (viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer