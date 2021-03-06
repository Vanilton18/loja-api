"""loja_virtual URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from produtos.api.viewsets import ProdutoViewSet
from pedidos.api.viewsets import PedidoViewSet
from accounts.api import viewsets
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'produtos', ProdutoViewSet, base_name='Produtos')
router.register(r'pedidos', PedidoViewSet)
router.register(r'users', viewsets.SignupViewSet, base_name='account-create')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('token/', obtain_auth_token)
]
