from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.parsers import MultiPartParser,FormParser
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import *
from .models import *
from .serializers import *
# Create your views here.

class EmpleadoViewset(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    parser_classes = (MultiPartParser,FormParser)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre']
    ordering_fields = ['id']
    

class ClienteViewset(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    parser_classes = (MultiPartParser,FormParser)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre']
    ordering_fields = ['id']
    
class UserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser,FormParser)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['username']
    ordering_fields = ['id']

    