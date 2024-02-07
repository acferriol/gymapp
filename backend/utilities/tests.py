from django.test import TestCase
from datetime import datetime, timedelta
from .models import Notifications, Plan, Pagos, ClaseParticular, ClaseGrupo
from actors.models import Empleado, Cliente
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Notifications, Plan, Pagos, ClaseParticular, ClaseGrupo
from actors.models import Empleado, Cliente
from datetime import datetime
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class NotificationsModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user1 = User.objects.create_user(username='testuser1', password='testpassword1')
        self.remitente = Empleado.objects.create(nombre='John', apellidos='Doe', telefono='12345678', dni='12345678901', labor='Supervisor',user=self.user)
        self.destinatario = Empleado.objects.create(nombre='Jane', apellidos='Smith', telefono='98765432', dni='98765432109', labor='Otro',user=self.user1)

    def test_notifications_model(self):
        notification = Notifications.objects.create(remitente=self.remitente, mensaje='Mensaje de prueba')
        notification.destinatarios.add(self.destinatario)
        notification.save()

        self.assertEqual(str(notification), f"De {self.remitente} a las {notification.created_at}")
        self.assertEqual(notification.remitente, self.remitente)
        self.assertEqual(notification.destinatarios.count(), 1)
        self.assertEqual(notification.destinatarios.first(), self.destinatario)
        self.assertFalse(notification.recibido)
        self.assertEqual(notification.mensaje, 'Mensaje de prueba')

class PlanModelTest(TestCase):
    def test_plan_model(self):
        plan = Plan.objects.create(tipo_memb='Membresía Gold', precio=29.99, descripcion='Descripción de prueba')

        self.assertEqual(str(plan), 'Membresía Gold')
        self.assertEqual(plan.tipo_memb, 'Membresía Gold')
        self.assertEqual(plan.precio, 29.99)
        self.assertEqual(plan.descripcion, 'Descripción de prueba')

class PagosModelTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(nombre='John', apellidos='Doe', telefono='12345678', dni='12345678901', fecha_nacimiento=datetime.now().date())
        self.plan = Plan.objects.create(tipo_memb='Membresía Gold', precio=29.99, descripcion='Descripción de prueba')

    def test_pagos_model(self):
        pago = Pagos.objects.create(cliente=self.cliente, plan=self.plan, importe=29.99)

        self.assertEqual(str(pago), f"{self.cliente} -> {self.plan}")
        self.assertEqual(pago.cliente, self.cliente)
        self.assertEqual(pago.plan, self.plan)
        self.assertEqual(pago.importe, 29.99)
        self.assertEqual(pago.fecha_pago, datetime.now().date())
        self.assertEqual(pago.fecha_vence, pago.fecha_pago + timedelta(days=30))

class ClaseParticularModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.cliente = Cliente.objects.create(nombre='John', apellidos='Doe', telefono='12345678', dni='12345678901', fecha_nacimiento=datetime.now().date())
        self.empleado = Empleado.objects.create(nombre='Jane', apellidos='Smith', telefono='98765432', dni='98765432109', labor='Instructor',user=self.user)

    def test_clase_particular_model(self):
        hora = datetime.now()
        clase_particular = ClaseParticular.objects.create(cliente=self.cliente, empleado=self.empleado, hora=hora, descripcion='Descripción de prueba')

        self.assertEqual(str(clase_particular), f"{self.cliente} - {self.empleado}")
        self.assertEqual(clase_particular.cliente, self.cliente)
        self.assertEqual(clase_particular.empleado, self.empleado)
        self.assertEqual(clase_particular.hora, hora)
        self.assertEqual(clase_particular.descripcion, 'Descripción de prueba')

class ClaseGrupoModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.empleado = Empleado.objects.create(nombre='Jane', apellidos='Smith', telefono='98765432', dni='98765432109', labor='Instructor',user=self.user)
        self.cliente1 = Cliente.objects.create(nombre='John', apellidos='Doe', telefono='12345678', dni='12345678901', fecha_nacimiento=datetime.now().date())
        self.cliente2 = Cliente.objects.create(nombre='Alice', apellidos='Johnson', telefono='87654321', dni='10987654321', fecha_nacimiento=datetime.now().date())

    def test_clase_grupo_model(self):
        hora = datetime.now()
        clase_grupo = ClaseGrupo.objects.create(empleado=self.empleado, hora=hora, descripcion='Descripción de prueba', capacity=10)
        clase_grupo.clientes.add(self.cliente1, self.cliente2)
        clase_grupo.save()

        self.assertEqual(str(clase_grupo), f"{self.empleado} a las {hora}")
        self.assertEqual(clase_grupo.hora, hora)
        self.assertEqual(clase_grupo.descripcion, 'Descripción de prueba')
        self.assertEqual(clase_grupo.capacity, 10)
        self.assertEqual(clase_grupo.clientes.count(), 2)
        self.assertIn(self.cliente1, clase_grupo.clientes.all())
        self.assertIn(self.cliente2, clase_grupo.clientes.all())



#
class NotificationViewSetTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.get(user=self.user)
        self.user1 = User.objects.create_user(username='testuser1', password='testpassword1')
        self.token1 = Token.objects.get(user=self.user1)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.remitente = Empleado.objects.create(nombre='John', apellidos='Doe', telefono='12345678', dni='12345678901', labor='Supervisor',user=self.user)
        self.destinatario = Empleado.objects.create(nombre='Jane', apellidos='Smith', telefono='98765432', dni='98765432109', labor='Otro',user=self.user1)
        self.notification = Notifications.objects.create(remitente=self.remitente, mensaje='Mensaje de prueba')
        self.notification.destinatarios.add(self.destinatario)

    def test_get_notifications(self):
        response = self.client.get('/notifications/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_notification(self):
        data = {
            'remitente': self.remitente.id,
            'destinatarios': [self.destinatario.id],
            'mensaje': 'Nuevo mensaje'
        }
        response = self.client.post('/notifications/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_notification(self):
        data = {
            'mensaje': 'Mensaje actualizado'
        }
        response = self.client.patch(f'/notifications/{self.notification.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['mensaje'], 'Mensaje actualizado')

    def test_delete_notification(self):
        response = self.client.delete(f'/notifications/{self.notification.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PlanViewSetTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.get(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.plan = Plan.objects.create(tipo_memb='Membresía Gold', precio=29.99, descripcion='Descripción de prueba')

    def test_get_plans(self):
        response = self.client.get('/plan/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_plan(self):
        data = {
            'tipo_memb': 'Membresía Silver',
            'precio': 19.99,
            'descripcion': 'Descripción de prueba'
        }
        response = self.client.post('/plan/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_plan(self):
        data = {
            'precio': 39.99
        }
        response = self.client.patch(f'/plan/{self.plan.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['precio'], 39.99)

    def test_delete_plan(self):
        response = self.client.delete(f'/plan/{self.plan.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PagosViewSetTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.get(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.cliente = Cliente.objects.create(nombre='John', apellidos='Doe', telefono='12345678', dni='12345678901', fecha_nacimiento=datetime.now().date())
        self.plan = Plan.objects.create(tipo_memb='Membresía Gold', precio=29.99, descripcion='Descripción de prueba')
        self.pago = Pagos.objects.create(cliente=self.cliente, plan=self.plan, importe=29.99)

    def test_get_pagos(self):
        response = self.client.get('/pagos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_pago(self):
        data = {
            'cliente': self.cliente.id,
            'plan': self.plan.id,
            'importe': 29.99
        }
        response = self.client.post('/pagos/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_pago(self):
        data = {
            'importe': 39.99
        }
        response = self.client.patch(f'/pagos/{self.pago.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['importe'], 39.99)

    def test_delete_pago(self):
        response = self.client.delete(f'/pagos/{self.pago.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ClaseParticularViewSetTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.get(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.cliente = Cliente.objects.create(nombre='John', apellidos='Doe', telefono='12345678', dni='12345678901', fecha_nacimiento=datetime.now().date())
        self.empleado = Empleado.objects.create(nombre='Jane', apellidos='Smith', telefono='98765432', dni='98765432109', labor='Otro',user = self.user)
        self.hora = datetime.now()
        self.clase_particular = ClaseParticular.objects.create(empleado=self.empleado, cliente=self.cliente, hora=self.hora)

    def test_get_clases_particulares(self):
        response = self.client.get('/clases_particulares/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class ClaseGrupoViewSetTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.get(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.hora = datetime.now()
        self.empleado = Empleado.objects.create(nombre='John', apellidos='Doe', telefono='12345678', dni='12345678901', labor='Otro',user = self.user)
        self.cliente1 = Cliente.objects.create(nombre='Jane', apellidos='Smith', telefono='98765432', dni='98765432109', fecha_nacimiento=datetime.now().date())
        self.cliente2 = Cliente.objects.create(nombre='Alice', apellidos='Johnson', telefono='55555555', dni='55555555555', fecha_nacimiento=datetime.now().date())
        self.clase_grupo = ClaseGrupo.objects.create(empleado=self.empleado,hora=self.hora,capacity=20)
        self.clase_grupo.clientes.add(self.cliente1, self.cliente2)

    def test_get_clases_grupo(self):
        response = self.client.get('/clases_grupo/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_clase_grupo(self):
        data = {
            'empleado': self.empleado.id
        }
        response = self.client.patch(f'/clases_grupo/{self.clase_grupo.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['empleado'], self.empleado.id)

    def test_delete_clase_grupo(self):
        response = self.client.delete(f'/clases_grupo/{self.clase_grupo.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)