from django.urls import path
from . import views

app_name ="carro"

urlpatterns = [
        path('agregar/<int:id>/', views.agregar, name='agregar'),
        path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
        path('restar/<int:id>/', views.restar, name='restar'),   
        path('vaciar/', views.vaciar, name='vaciar'),
]