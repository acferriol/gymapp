from rest_framework import serializers
from actors.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields= ['id','username','email','authorization']
        depth = 1

class EmpleadoSerializer(serializers.ModelSerializer):
    id=serializers.UUIDField(default=uuid.uuid4)
    foto = serializers.ImageField(default='media/empleado_default.svg')

    class Meta:
        model = Empleado
        fields= '__all__'
        depth = 1

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields= '__all__'
        depth = 1