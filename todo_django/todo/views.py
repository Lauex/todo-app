from django.shortcuts import render

from .models import Todo
from .serializers import TodoSerializer

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class TodoViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
