from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="inicio"),

    path('motos/', Moto, name="motos"),
    path('taller/', Taller, name="taller"),

    path('moto_form/', MotoForm, name="moto_form"),
    path('curso_form2/', MotoForm2, name="moto_form2"),

  
#_______________________
    path('accesorios/', accesorios, name="accesorios"),
    path('update_accesorio/<id_accesorio>/', updateAccesorios, name="update_accesorio"),
     path('delete_accesorio/<id_accesorio>/', deleteAccesorio, name="delete_accesorio"),
    path('create_accesorio/', createAccesorio, name="create_accesorio"),

    path('cliente/', ClienteList.as_view(), name="cliente"),
    path('create_cliente/', ClienteCreate.as_view(), name="create_cliente"),
    path('detail_cliente/<int:pk>/', ClienteDetail.as_view(), name="detail_cliente"),
    path('update_cliente/<int:pk>/', ClienteUpdate.as_view(), name="update_cliente"),
    path('delete_cliente/<int:pk>/', ClienteDelete.as_view(), name="delete_cliente"),
]
