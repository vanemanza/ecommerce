from django.contrib import admin
from .models import Categoria, Producto

class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=("created", "updated")    

admin.site.register(Categoria, CategoriaProdAdmin)
admin.site.register(Producto, ProductoAdmin)