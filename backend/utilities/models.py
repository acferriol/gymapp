from django.db import models
from actors.models import Model,Empleado,Cliente
from datetime import datetime
import datetime as dt
# Create your models here.

class Notifications(Model):
    remitente = models.ForeignKey(Empleado,on_delete=models.DO_NOTHING,related_name="send_rev")
    destinatarios = models.ManyToManyField(Empleado,related_name="recib_rev")
    recibido = models.BooleanField('Recibido', default=False)
    mensaje = models.TextField(null=False,blank=False)
    created_at = models.DateTimeField(default=datetime.now())


class Plan(Model):
    tipo_memb = models.CharField(max_length=30, null=False)
    precio = models.FloatField(null=False,blank=False)
    descripcion = models.TextField(null=False,blank=False)


class Pagos(Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.DO_NOTHING,related_name="pagos_cli_rev")
    plan = models.ForeignKey(Plan,on_delete=models.DO_NOTHING,related_name="pagos_plan_rev")
    fecha_pago = models.DateField(default=datetime.now().today().date())

    def get_vence(self):
        return self.fecha_pago + dt.timedelta(days=30)
    
    fecha_vence = property(get_vence)
    importe = models.FloatField(null=False,blank=False)


class ClaseParticular(Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.DO_NOTHING,related_name="clase_part_cli_rev")
    empleado = models.ForeignKey(Empleado,on_delete=models.DO_NOTHING,related_name="clase_part_emp_rev")
    hora = models.DateTimeField(null=False,blank=False)
    descripcion = models.CharField(max_length=100)

class ClaseGrupo(Model):
    empleado = models.ForeignKey(Empleado,on_delete=models.DO_NOTHING,related_name="clase_group_emp_rev")
    hora = models.DateTimeField(null=False,blank=False)
    descripcion = models.CharField(max_length=100,null=False,blank=False)
    capacity = models.IntegerField(null=False,blank=False)
    clientes = models.ManyToManyField(Cliente,related_name="clase_group_cli_rev")