from django.db import models
from actors.models import Model,Empleado
import datetime
# Create your models here.

class Notifications(Model):
    remitente = models.ForeignKey(Empleado,on_delete=models.DO_NOTHING,related_name="notifications")
    destinatarios = models.ManyToManyField(Empleado,related_name="all_notes")
    recibido = models.BooleanField('Recibido', default=False)
    mensaje = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())