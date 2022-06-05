from django.contrib import admin
from Productos.models import producto,  categoria

# Register your models here.

admin.site.register(producto)
admin.site.register(categoria)