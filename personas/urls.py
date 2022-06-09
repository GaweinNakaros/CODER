

from django.urls import path
from . import views


urlpatterns = [

    path("inicio", views.inicio , name="inicio"),
    path("amigos", views.lista_amigos , name="amigos"),
    path("familia", views.lista_familiares , name="familia"),
    path("clientes", views.lista_clientes , name="clientes"),
    path("alta_clientes", views.alta_clientes , name="alta_clientes"),
    path("alta_familiar", views.alta_familiar , name="alta_familiar"),
    path("alta_amigos", views.alta_amigos , name="alta_amigos"),
    path("busqueda",     views.busqueda , name="busqueda" ),
    path("buscar",     views.buscar , name="buscar" ),
    #path("eliminar_familiar/<int:id>" , views.eliminar_familiar , name ="eliminar_familiar"),
    ##path("editar_familiar/<int:id>" , views.editar ,  name="editar_familiar"),
    ##path(),
]