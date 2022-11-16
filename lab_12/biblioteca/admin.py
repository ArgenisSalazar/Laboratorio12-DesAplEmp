from django.contrib import admin

# Register your models here.
from .models import Autor,Prestamos,Libro,Usuario,LibroPrestamo,UsuarioPrestamo

class LibroPrestamoInline(admin.TabularInline):
    model = LibroPrestamo
    extra = 1

class UsuarioPrestamoInline(admin.TabularInline):
    model = UsuarioPrestamo
    extra = 1

class LibroAdmin(admin.ModelAdmin):
    list_display=("idLibro","codigo","titulo","isbn","editorial","numpags")
    search_fields=("idLibro","titulo")
    list_filter=("editorial",)
    
class UsuarioAdmin(admin.ModelAdmin):
    list_display=("idUsuario","numUsuario","nif","nombre","direccion","telefono")
    search_fields=("idUsuario","nombre")

class AutorAdmin(admin.ModelAdmin):
    list_display=("idAutor","nombre","nacionalidad","libro")
    search_fields=("idAutor","nombre")
    list_filter=("nacionalidad",)
    
class PrestamosAdmin(admin.ModelAdmin):
    inlines = [LibroPrestamoInline,UsuarioPrestamoInline,]
    list_display=("idPrestamo","idLibro","idUsuario","FecPrestamo","FecDevolucion")
    search_fields=("idPrestamo","idLibro")
    filter_horizontal = ['libro','usuario',]

admin.site.register(Libro,LibroAdmin)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Prestamos,PrestamosAdmin)