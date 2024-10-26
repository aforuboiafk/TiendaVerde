"""
URL configuration for TiendaVerde project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from core.views import home, productos,carrito,inicio_sesion,cuenta, register, cerrar_sesion, agregar_producto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('productos/',productos, name='productos'),
    path('carrito/',carrito, name='carrito'),
    path('login/',inicio_sesion, name='login'),
    path('logout/',cerrar_sesion, name='logout'),
    path('register/',register, name='register'),
    path('cuenta/',cuenta, name='cuenta'),
    path('productos/<int:id>', agregar_producto, name='agregar'), 

]
