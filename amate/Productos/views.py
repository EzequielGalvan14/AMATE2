from django.shortcuts import render
from Productos.models import producto
# Create your views here.

def Productos(request):
        productos = producto.objects.all()
        context = {'productos':productos}
        return render(request, 'products.html', context=context)