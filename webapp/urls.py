
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('servicios', views.servicios, name='servicios'),
    path('blog', views.blog, name='blog'),
    path('contacto', views.contacto, name='contacto'),
    path('tienda', views.tienda, name='tienda'),   
]