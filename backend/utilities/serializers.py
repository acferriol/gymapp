from rest_framework import serializers
from utilities.models import *

class NotificationsSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = Pagos
        fields= '__all__'
        depth = 1

class ClaseParticularSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaseParticular
        fields= '__all__'
        depth = 1

class ClaseGrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaseGrupo
        fields= '__all__'
        depth = 1