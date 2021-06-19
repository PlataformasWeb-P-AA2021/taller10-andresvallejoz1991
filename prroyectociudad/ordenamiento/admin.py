from django.contrib import admin
from ordenamiento.models import Parroquia, Barrio
from import_export.admin import ImportExportModelAdmin

class ParroquiaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase
    list_display = ('nombre','tipo_parroquia')
    search_fields = ('nombre','tipo_parroquia')

admin.site.register(Parroquia, ParroquiaAdmin)

class BarrioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('nombre', 'num_viviendas', 'parques','num_edificios')
    search_fields = ('parroquia__nombre','nombre')

admin.site.register(Barrio, BarrioAdmin)
