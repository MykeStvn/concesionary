from django.urls import path

from .import views

urlpatterns = [
    path('',views.inicio, name="inicio"),
    #ciudades
    path('listadoCiudades/',views.listadoCiudades,name='listadoCiudades'),
    path('agregar_ciudad/',views.agregar_ciudad,name='agregar_ciudad'),
    path('get_city_data/', views.get_city_data, name='get_city_data'),
    path('update_city/', views.update_city, name='update_city'),
    path('delete_city/', views.delete_city, name='delete_city'),
    #modelos
    path('listadoModelos/',views.listadoModelos,name='listadoModelos'),
    path('agregar_modelo/',views.agregar_modelo,name='agregar_modelo'),
    path('get_model_data/',views.get_model_data,name='get_model_data'),
    path('update_model/',views.update_model,name='update_model'),
    path('delete_model/',views.delete_model,name='delete_model'),
    #propiertarios
    path('listadoPropietarios',views.listadoPropietarios,name='listadoPropietarios'),
    path('add_propierty/', views.add_propierty, name='add_propierty'),
    path('get_propierty_data/', views.get_propierty_data, name='get_propierty_data'),
    path('update_propierty/', views.update_propierty, name='update_propierty'),
    path('delete_propierty/', views.delete_propierty, name='delete_propierty'),


    #vehiculos
    path('listadoVehiculos',views.listadoVehiculos,name='listadoVehiculos'),
]
