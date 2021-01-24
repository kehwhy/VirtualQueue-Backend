from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, LineSerializer
from .models import User, Line

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer

class LineViewSet(viewsets.ModelViewSet):
    queryset = Line.objects.all().order_by('id')
    serializer_class = LineSerializer