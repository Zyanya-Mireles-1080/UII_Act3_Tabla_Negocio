from django.urls import path
from proveedores_app import views 

urlpatterns = [
    path('',views.inicio_vista, name="inicio_vista"),
    path("registrarProveedores/",views.registrarProveedores,name="registrarProveedores"),
    path("seleccionarProveedores/<id_proveedor>",views.seleccionarProveedores,name="seleccionarProveedores"),
    path("editarProveedores/",views.editarProveedores,name="editarProveedores"),
    path("borrarProveedores/<id_proveedor>",views.borrarProveedores,name="borrarProveedores"),
]