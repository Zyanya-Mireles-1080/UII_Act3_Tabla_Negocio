from django.urls import path
from pedidos_app import views 

urlpatterns = [
    path('',views.inicio_vista, name="inicio_vista"),
    path("registrarPedidos/",views.registrarPedidos,name="registrarPedidos"),
    path("seleccionarPedidos/<id_pedido>",views.seleccionarPedidos,name="seleccionarPedido"),
    path("editarPedidos/",views.editarPedidos,name="editarPedidos"),
    path("borrarPedidos/<id_pedido>",views.borrarPedidos,name="borrarPedidos"),
]