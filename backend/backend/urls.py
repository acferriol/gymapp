"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from actors.views import *
from utilities.views import *
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()

router.register("empleados",EmpleadoViewset,basename="empleados")
router.register("users",UserViewset,basename="users")
router.register("clientes",ClienteViewset,basename="clientes")
router.register("notifications",NotificationViewset,basename="notifications")
router.register("plan",PlanViewset,basename="planes")
router.register("pagos",PagosViewset,basename="pagos")
router.register("clases_particulares",ClaseParticularViewset,basename="clases_particulares")
router.register("clases_grupo",ClaseGrupoViewset,basename="clases_grupo")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-token-auth", obtain_auth_token),
    path("login/",LoginView.as_view(),name="login"),
    path("",include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
