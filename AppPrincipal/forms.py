from typing import Any
from django import forms
from .models import *
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class ClienteForm (forms.Form):
    nombre = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=200)
    telefono = forms.CharField(max_length=20)
    correo_electronico = forms.EmailField()
    numero_cliente = forms.CharField(max_length=20)
    historial_pedidos = forms.Textarea()
    
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'servicios_solicitados', 'fecha_solicitud', 'fecha_entrega_deseada', 'estado_pedido']
        
        widgets = {
            'fecha_solicitud': forms.DateInput(attrs={'type': 'date'}),
            'fecha_entrega_deseada': forms.DateInput(attrs={'type': 'date'}),
            
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'direccion', 'telefono', 'correo_electronico', 'fecha_contratacion', 'historial_empleo', 'capacitaciones']
        
        
        widgets = {
            'fecha_contratacion': forms.DateInput(attrs={'type': 'date'}),
            
        }


class ProgramacionForm(forms.ModelForm):
    class Meta:
        model = Programacion
        fields = ['pedido', 'proveedor_asignado', 'fecha_hora_programada']
        
        widgets = {
            'fecha_hora_programada': forms.DateInput(attrs={'type': 'date'}),
                       
        }
        
        
class RegistroTratamientoForm(forms.ModelForm):
    class Meta:
        model = RegistroTratamiento
        fields = ['pedido_asociado', 'fecha_hora_inicio', 'fecha_hora_finalizacion', 'temperatura', 'tiempo_tratamiento', 'resultados']
        
        widgets = {
            'fecha_hora_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_hora_finalizacion': forms.DateInput(attrs={'type': 'date'}),
                        
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personaliza el widget de fecha y hora para que sea más fácil de usar
        self.fields['fecha_hora_inicio'].widget.attrs.update({'class': 'datetimepicker'})
        self.fields['fecha_hora_finalizacion'].widget.attrs.update({'class': 'datetimepicker'})

        # Personaliza el widget de texto para el campo "resultados"
        self.fields['resultados'].widget = forms.Textarea(attrs={'rows': 4})

# Nota: Asegúrate de tener una clase "datetimepicker" en tus archivos de hoja de estilo CSS para personalizar los campos de fecha y hora.

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['pedido_asociado', 'total_pagar', 'fecha_emision']
        
        widgets = {
            'fecha_emision': forms.DateInput(attrs={'type': 'date'}),
                     
        }
        
        
        
        
class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['tipo_documento', 'fecha_emision', 'asociado_pedido']
        
        widgets = {
            'fecha_emision': forms.DateInput(attrs={'type': 'date'}),
                   
        }
        
    def __init__(self, cliente, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['asociado_pedido'].queryset = Pedido.objects.filter(cliente=cliente)
        
        
        
class RegistroCalidadForm(forms.ModelForm):
    class Meta:
        model = RegistroCalidad
        fields = ['pedido_o_tratamiento_asociado', 'resultados_pruebas', 'responsable_prueba']
        
        
class CapacitacionForm(forms.ModelForm):
    class Meta:
        model = Capacitacion
        fields = ['nombre', 'fecha', 'descripcion']

        labels = {
            'nombre': 'Nombre de la Capacitación',
            'fecha': 'Fecha de la Capacitación',
            'descripcion': 'Descripción de la Capacitación',
        }

        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            
        }
        
        
class ServicioTratamientoForm(forms.ModelForm):
    class Meta:
        model = ServicioTratamiento
        fields = ['tipo_servicio', 'descripcion', 'parametros_tratamiento', 'equipo_requerido']
        
        
class UserEditForm(UserChangeForm):
    password = forms.CharField(
        
        help_text="",
        widget=forms.HiddenInput(), required=False
    )
    
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña" , widget=forms.PasswordInput)
    
    class Meta:
        model= User
        fields = ["first_name", "last_name", "email","password1","password2" ]
        
        
    def clean_password2(self):
        
        self.cleaned_data
        
        password1= self.cleaned_data["password1"]
        password2= self.cleaned_data["password2"]
        
        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        
        return password2
    
    
class AvatarForms(forms.ModelForm):
    
      
    class Meta:
        model= Avatar
        fields = ["imagen",]
    