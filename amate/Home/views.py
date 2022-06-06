from django.shortcuts import render
from Productos.models import producto
from Home.models import Publicacion
# Create your views here.

def home(request):
        publicaciones = Publicacion.objects.all()
        context = {'publicaciones':publicaciones}
        return render(request, 'index.html', context=context)
