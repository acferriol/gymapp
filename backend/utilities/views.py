from django.shortcuts import render
from .models import *
from .serializers import *
from actors.permissions import AuthorizationPermission
from rest_framework.parsers import *
from rest_framework.filters import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class NotificationViewset(viewsets.ModelViewSet):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer
    parser_classes = (MultiPartParser,FormParser)
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend]
    search_fields = ['remitente','destinatarios']
    ordering_fields = ['id']
    filterset_fields = ['remitente','destinatarios']
    permission_classes = (IsAuthenticated)

class PlanViewset(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    parser_classes = (MultiPartParser,FormParser)
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['tipo_memb']
    ordering_fields = ['id']
    permission_classes = (IsAuthenticated)

class PagosViewset(viewsets.ModelViewSet):
    queryset = Pagos.objects.all()
    serializer_class = PagosSerializer
    parser_classes = (MultiPartParser,FormParser)
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend]
    search_fields = ['cliente','plan']
    ordering_fields = ['id']
    filterset_fields = ['cliente','plan']
    permission_classes = (IsAuthenticated)

class ClaseParticularViewset(viewsets.ModelViewSet):
    queryset = ClaseParticular.objects.all()
    serializer_class = ClaseParticularSerializer
    parser_classes = (MultiPartParser,FormParser)
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend]
    search_fields = ['empleado','cliente']
    ordering_fields = ['id']
    filterset_fields = ['empleado','cliente']
    permission_classes = (IsAuthenticated)

class ClaseGrupoViewset(viewsets.ModelViewSet):
    queryset = ClaseGrupo.objects.all()
    serializer_class = ClaseGrupoSerializer
    parser_classes = (MultiPartParser,FormParser)
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend]
    search_fields = ['empleado','clientes']
    ordering_fields = ['id']
    filterset_fields = ['empleado']
    permission_classes = (IsAuthenticated)