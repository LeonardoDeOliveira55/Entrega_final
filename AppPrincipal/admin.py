from django.contrib import admin
from .models import *

class cliente_admin(admin.ModelAdmin):
    list_display = ['nombre', 'correo_electronico']
    search_fields = ['nombre']
    list_filter = ['nombre']
    

admin.site.register(Cliente, cliente_admin)
admin.site.register(Proveedor)
admin.site.register(ServicioTratamiento)
admin.site.register(Pedido)
admin.site.register(Programacion)
admin.site.register(RegistroTratamiento)
admin.site.register(EquipoTratamiento)
admin.site.register(Factura)
admin.site.register(Pago)
admin.site.register(Documento)
admin.site.register(RegistroCalidad)
admin.site.register(Empleado)
admin.site.register(Capacitacion)
admin.site.register(Avatar)
