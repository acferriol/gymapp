from rest_framework import serializers
from utilities.models import *

class NotificationsSerializer(serializers.ModelSerializer):
    remitente = serializers.SlugRelatedField(
        many = False,
        read_only=False,
        queryset = Empleado.objects.all(),
        slug_field='id')
    
    destinatarios = serializers.SlugRelatedField(
        many = True,
        read_only=False,
        queryset = Empleado.objects.all(),
        slug_field='id')

    class Meta:
        model = Notifications
        fields = '__all__'
        depth = 1

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields= '__all__'
        depth = 1

class PagosSerializer(serializers.ModelSerializer):
    cliente = serializers.SlugRelatedField(
        many = False,
        read_only=False,
        queryset = Cliente.objects.all(),
        slug_field='id')
    
    plan = serializers.SlugRelatedField(
        many = False,
        read_only=False,
        queryset = Plan.objects.all(),
        slug_field='id')

    class Meta:
        model = Pagos
        fields= '__all__'
        depth = 1

class ClaseParticularSerializer(serializers.ModelSerializer):
    empleado = serializers.SlugRelatedField(
        many = False,
        read_only=False,
        queryset = Empleado.objects.all(),
        slug_field='id')
    
    cliente = serializers.SlugRelatedField(
        many = False,
        read_only=False,
        queryset = Cliente.objects.all(),
        slug_field='id')
    
    class Meta:
        model = ClaseParticular
        fields= '__all__'
        depth = 1

class ClaseGrupoSerializer(serializers.ModelSerializer):
    empleado = serializers.SlugRelatedField(
        many = False,
        read_only=False,
        queryset = Empleado.objects.all(),
        slug_field='id')
    
    clientes = serializers.SlugRelatedField(
        many = True,
        read_only=False,
        queryset = Cliente.objects.all(),
        slug_field='id')

    class Meta:
        model = ClaseGrupo
        fields= '__all__'
        depth = 1