from django.urls import path

from Productos.views import Productos

urlpatterns =[
    path('', Productos, name = 'products'),
]