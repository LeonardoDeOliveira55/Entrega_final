from django.db import models
from django.contrib.auth.models import User

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    correo_electronico = models.EmailField()

    class Meta:
        abstract = True
        
        
    def __str__(self):
        return f'{self.nombre} - {self.correo_electronico}'


class Cliente(Persona):
    numero_cliente = models.CharField(max_length=20, unique=True)
    historial_pedidos = models.TextField()
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ('nombre',)
        unique_together = ('numero_cliente','correo_electronico')


class Proveedor(Persona):
    nombre_empresa = models.CharField(max_length=100)
    contacto_principal = models.CharField(max_length=100)
    servicios_proporcionados = models.TextField()
    
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
    
    def __str__(self):
        return f'{self.nombre_empresa}'


class ServicioTratamiento(models.Model):
    tipo_servicio = models.CharField(max_length=50)
    descripcion = models.TextField()
    parametros_tratamiento = models.TextField()
    equipo_requerido = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.tipo_servicio}'


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicios_solicitados = models.ManyToManyField(ServicioTratamiento)
    fecha_solicitud = models.DateField()
    fecha_entrega_deseada = models.DateField()
    estado_pedido = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.cliente} - N° Pedido: {self.pk}'


class Programacion(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    proveedor_asignado = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_hora_programada = models.DateTimeField()
    
    def __str__(self):
        return f'{self.pedido} - {self.proveedor_asignado}'
    
    class Meta:
        verbose_name = 'Programacion'
        verbose_name_plural = 'Programaciones'
    



class RegistroTratamiento(models.Model):
    pedido_asociado = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    fecha_hora_inicio = models.DateTimeField()
    fecha_hora_finalizacion = models.DateTimeField()
    temperatura = models.DecimalField(max_digits=8, decimal_places=2)
    tiempo_tratamiento = models.DurationField()
    resultados = models.TextField()
    
    def __str__(self):
        return f'{self.pedido_asociado}'


class EquipoTratamiento(models.Model):
    nombre_equipo = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nombre_equipo}'


class Factura(models.Model):
    pedido_asociado = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    total_pagar = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_emision = models.DateField()
    
    def __str__(self):
        return f'{self.pedido_asociado}'


class Pago(models.Model):
    factura_asociada = models.ForeignKey(Factura, on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    metodo_pago = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.factura_asociada}'


class Documento(models.Model):
    tipo_documento = models.CharField(max_length=50)
    fecha_emision = models.DateField()
    asociado_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)  
    
    def __str__(self):
        return f'{self.asociado_pedido}'


class RegistroCalidad(models.Model):
    pedido_o_tratamiento_asociado = models.ForeignKey(Pedido, on_delete=models.CASCADE)  
    resultados_pruebas = models.TextField()
    responsable_prueba = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.pedido_o_tratamiento_asociado}'
    
    class Meta:
        verbose_name = 'Registro de Calidad'
        verbose_name_plural = 'Registros de Calidad'


class Empleado(Persona):
    fecha_contratacion = models.DateField()
    historial_empleo = models.TextField()
    capacitaciones = models.ManyToManyField('Capacitacion')


class Capacitacion(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    descripcion = models.TextField()
    
    def __str__(self):
        return f'{self.nombre} - {self.fecha} - {self.descripcion}'
    
    class Meta:
        verbose_name = 'Capacitacion'
        verbose_name_plural = 'Capacitaciones'

class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="Avatares", height_field= None, width_field=None, max_length=None, blank=True, null=True)