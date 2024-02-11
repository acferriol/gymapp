from django.test import TestCase
from datetime import date
from .models import CustomUser, Empleado, Cliente
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.urls import reverse
from .models import Empleado, Cliente
from .serializers import EmpleadoSerializer, ClienteSerializer

User = get_user_model()

class CustomUserModelTest(TestCase):
    def test_str_representation(self):
        user = CustomUser(username='john')
        self.assertEqual(str(user), 'john')

class EmpleadoModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='johndoe')
        self.empleado = Empleado.objects.create(
            nombre='John',
            apellidos='Doe',
            telefono='12345678',
            dni='12345678901',
            labor='Supervisor',
            user=self.user
        )

    def test_str_representation(self):
        self.assertEqual(str(self.empleado), 'John Doe')

    def test_empleado_has_user(self):
        self.assertEqual(self.empleado.user, self.user)

class ClienteModelTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nombre='Jane',
            apellidos='Doe',
            telefono='98765432',
            dni='98765432109',
            fecha_nacimiento=date(1990, 1, 1),
        )

    def test_str_representation(self):
        self.assertEqual(str(self.cliente), 'Jane Doe')

    def test_cliente_has_empleados(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user1 = User.objects.create_user(username='testuser1', password='testpassword1')

        empleado1 = Empleado.objects.create(
            nombre='John',
            apellidos='Doe',
            telefono='12345678',
            dni='12345678901',
            labor='Supervisor',
            user = self.user
        )
        empleado2 = Empleado.objects.create(
            nombre='Alice',
            apellidos='Smith',
            telefono='87654321',
            dni='10987654321',
            labor='Entrenador',
            user = self.user1
        )
        self.cliente.empleados.add(empleado1, empleado2)
        self.assertIn(empleado1, self.cliente.empleados.all())
        self.assertIn(empleado2, self.cliente.empleados.all())




class EmpleadoViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser2', password='testpassword2')
        self.token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.empleado = Empleado.objects.create(
            nombre='John',
            apellidos='Doe',
            telefono='12345678',
            dni='12345678901',
            labor='Supervisor',
            user=self.user
        )

    def test_list_empleados(self):
        url = reverse('empleados-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nombre'], 'John')

    def test_retrieve_empleado(self):
        url = reverse('empleados-detail', kwargs={'pk': self.empleado.pk})
        #print(url)
        response = self.client.get(url)
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN) #No tiene permiso por la authorization




class ClienteViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser3', password='testpassword3')
        self.token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.cliente = Cliente.objects.create(
            nombre='Jane',
            apellidos='Doe',
            telefono='98765432',
            dni='98765432109',
            fecha_nacimiento=date(1990, 1, 1),
        )

    def test_list_clientes(self):
        url = reverse('clientes-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nombre'], 'Jane')

    def test_retrieve_cliente(self):
        url = reverse('clientes-detail', kwargs={'pk': self.cliente.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], 'Jane')



class LoginViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser4', password='testpassword4')
        self.token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        

    def test_login(self):
        url = reverse('login')
        #print(url)
        data = {'username': 'testuser4', 'password': 'testpassword4'}
        response = self.client.post(url, data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_invalid_credentials(self):
        url = reverse('login')
        data = {'username': 'testuser', 'password': 'wrongpassword'}
        response = self.client.post(url, data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotIn('token', response.data)


#
#