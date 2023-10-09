from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('Opciones_clientes/', opciones_clietes, name="Opciones_clientes"), 
    path('Opciones_pedidos/', opciones_pedidos, name="Opciones_pedidos"),
    path('Opciones_empleados/', opciones_empleados, name="Opciones_empleados"),
    path('Opciones_provedores/', opciones_provedores, name="Opciones_provedores"),
    path('Contacto/', contacto, name="contacto"),
    path('agregar_avatar/', agregar_avatar, name="agregar_avatar"),
    
    
    
    path('Listar_clientes/', cliente_list, name="cliente_list"),
    path('Listar_pedidos/', pedido_list, name="pedido_list"),
    path('Listar_empleados/', empleado_list, name="empleado_list"),
    
    path('Crear_clientes/', cliente_create, name="cliente_create"),
    path('Crear_pedido/', pedido_create, name="pedido_create"),
    path('Crear_empleado/', empleado_create, name="empleado_create"),
    
    
    path('Detalle_clientes/<int:numero_cliente>/', cliente_detail , name="cliente_detail"),
    path('Detalle_pedido/<int:pk>/', pedido_detail , name="pedido_detail"),
    path('Detalle_empelado/<int:pk>/', empleado_detail , name="empelado_detail"),
    
    
    path('Editar_clientes/<int:numero_cliente>/', cliente_edit , name="cliente_edit"),
    path('Editar_pedido/<int:pk>/', pedido_edit , name="pedido_edit"),
    path('Editar_empleado/<int:pk>/', empleado_edit , name="empleado_edit"),
    
    path('Eliminar_clientes/<int:numero_cliente>/', cliente_delete , name="cliente_delete"),
    path('Eliminar_pedido/<int:pk>/', pedido_delete , name="pedido_delete"),
    path('Eliminar_empleado/<int:pk>/', empleado_delete , name="empleado_delete"),
    
    path('Pedidos_pendientes/', pedidos_pendientes , name="pedidos_pendientes"),
    
    path('Resultados_tratamientos/', resultados_tratamientos , name="resultados_tratamientos"),
    
    path('Programar_pedido/', programar_pedido , name="programar_pedido"),
    
    path('Registrar_Tratameinto/', registrar_tratamiento , name="registrar_tratamiento"),
    
    path('Facturar_pedido/', facturar_pedido, name="facturar_pedido"),
    
    path('Crear_documento/<int:pk>/', crear_documento, name="crear_documento"),
    
    path('Ver_certificados/<int:pk>/', ver_certificado, name="ver_certificado"),
    
    path('Resultados_calidad/', registrar_resultado_calidad, name="registrar_resultado_calidad"),
    
    path('Listar_capacitaciones/<int:empleado_id>/', listar_capacitaciones, name="listar_capacitaciones"),
    path('Detalle_capacitacion_empleado/<int:capacitacion_id>/<int:empelado_id>', detalle_capacitacion_empleado, name='detalle_capacitacion_empleado'),
    path('Crear_capacitacion/', crear_capacitacion, name='crear_capacitacion'),
    
    path('Sobre_mi/', sobre_mi, name='sobre_mi'),
    
    path('Login/', login_user, name='login'),
    path('Registrar/', register_user, name='register_user'),
    path('Logout/', LogoutView.as_view(template_name= 'logout.html'), name='logout'),
    path('Editar_user/', edit_user, name='edit_user'),
    
    
    path('Crear_servicio/', crear_servicio, name='crear_servicio'),
    path('Listar_servicio/', listar_servicio, name='listar_servicio'),
    path('Detalle_servicio/<int:numero_servicio>', detalle_servicio, name='detalle_servicio'),
    
    
    
    

        
]
