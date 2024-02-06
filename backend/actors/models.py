from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.


class Model(models.Model):
    
    class Meta:
        abstract=True


class CustomUser(AbstractUser):
    authorization = models.SmallIntegerField(null=True)
    def __str__(self):
        return self.username



TIPO_EMPLEADO = (("Supervisor","Supervisor"),("Entrenador","Entrenador"),("Otro","Otro"))

class Empleado(Model):
    nombre = models.CharField(max_length=30, null=False,blank=False)
    apellidos = models.CharField(max_length=50, null=False,blank=False,unique=True)
    telefono = models.CharField(max_length=8,unique=True)
    dni = models.CharField(max_length=11,unique=True,null=False,blank=False)
    labor = models.CharField(max_length=15, choices=TIPO_EMPLEADO)
    foto = models.ImageField(upload_to="media",default='media/empleado_default.svg')
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE, related_name="empleado_rev")

    def __str__(self) -> str:
        return self.nombre+" "+self.apellidos


class Cliente(Model):
    nombre = models.CharField(max_length=30, null=False,blank=False)
    apellidos = models.CharField(max_length=50, null=False,blank=False,unique=True)
    telefono = models.CharField(max_length=8,unique=True)
    dni = models.CharField(max_length=11,unique=True,null=False,blank=False)
    fecha_registro = models.DateField(default=datetime.now().today().date())
    fecha_nacimiento = models.DateField(null=False,blank=False)
    foto = models.ImageField(upload_to="media" ,default='media/empleado_default.svg')
    empleados = models.ManyToManyField(Empleado,related_name="clientes_rev",blank=False)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellidos}"