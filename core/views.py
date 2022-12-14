from rest_framework import viewsets
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, UserTaskSerializer, \
    ProfileSerializer, TaskSerializer

from .models import User, Profile, Task

class UserView(viewsets.ViewSet):
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class TaskViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, )
