from rest_framework import serializers
from actors.models import *


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields= ['id','username','password','email','authorization']
        depth = 1

class EmpleadoSerializer(serializers.ModelSerializer):
    foto = serializers.ImageField(default='media/empleado_default.svg')
    user = serializers.SlugRelatedField(
        many = False,
        read_only=False,
        queryset = CustomUser.objects.all(),
        slug_field='id')

    class Meta:
        model = Empleado
        fields= ['id','nombre', 'apellidos', 'telefono','dni', 'labor', 'foto', 'user']
        depth = 1

class ClienteSerializer(serializers.ModelSerializer):
    foto = serializers.ImageField(default='media/empleado_default.svg')
    empleados = serializers.SlugRelatedField(
        many = True,
        read_only=False,
        queryset = Empleado.objects.all(),
        slug_field='id')

    class Meta:
        model = Cliente
        fields= '__all__'
        depth = 1