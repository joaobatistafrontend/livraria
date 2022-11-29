from django.contrib import admin
from .models import Autor,Categoria, Compra, Editora, Livro, ItensCompra

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Livro)

class ItensInline(admin.TabularInline):
    model = ItensCompra


@admin.register(Compra)
class CompraAdm(admin.ModelAdmin):
    inlines = (ItensInline,)





