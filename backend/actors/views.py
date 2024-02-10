from django.shortcuts import render
from rest_framework import viewsets, filters, status
from rest_framework.parsers import MultiPartParser,FormParser
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import *
from django.contrib.auth import authenticate
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from .permissions import AuthorizationPermission
# Create your views here.

class EmpleadoViewset(viewsets.ModelViewSet):
    """
    Endpoints de la clase Empleado, GET,POST,PATCH,DELETE. Campos de busqueda [nombre, apellidos]
    Campos de orden [id]
    """
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    parser_classes = (MultiPartParser,FormParser)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre','apellidos']
    ordering_fields = ['id']
    permission_classes = (IsAuthenticated,AuthorizationPermission,)
    

class ClienteViewset(viewsets.ModelViewSet):
    """
    Endpoints de la clase Cliente, GET,POST,PATCH,DELETE Campos de busqueda [nombre, apellidos]
    Campos de orden [id]
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    parser_classes = (MultiPartParser,FormParser)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre','apellidos']
    ordering_fields = ['id']
    permission_classes = (IsAuthenticated,)
    
class UserViewset(viewsets.ModelViewSet):
    """
    Endpoints de la clase CustomUser, GET,POST,PATCH,DELETE Campos de busqueda [username]
    Campos de orden [id]
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser,FormParser)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['username']
    ordering_fields = ['id']
    permission_classes = (IsAuthenticated,AuthorizationPermission,)

class LoginView(APIView):
    """
    Endpoint login devuelve el token del usuario para propagarlo en las llamadas a la API
    """
    def post(self,request:Request):
        username = request.data.get('username')
        password = request.data.get("password")

        user = authenticate(username=username,password=password)
        if user is not None:
            response = {
                "message":"Login OK",
                "token":user.auth_token.key
            }
            return Response(data=response,status=status.HTTP_200_OK)
        else:
            return Response(data={"Credenciales invalidas"})



    def get(self,request:Request):
        content = {
            "user":str(request.user),
            "auth":str(request.auth)
        }

        return Response(data=content,status=status.HTTP_200_OK)


