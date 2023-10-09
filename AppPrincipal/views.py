from .forms import *
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth import update_session_auth_hash



from django.contrib.auth import login, logout, authenticate


def inicio (req):  
    
    try:
        avatar =  Avatar.objects.get(user=req.user) 
        return render (req,"inicio.html", {"url_avatar": avatar.imagen.url})
    
    except:
        return render (req,"inicio.html")
    


@staff_member_required(login_url='/app-inno-termic/Login/')
def opciones_clietes (req):
    
    return render (req, "Opciones_clientes.html")

@staff_member_required(login_url='/app-inno-termic/Login/')
def opciones_pedidos (req):
    
    return render (req, "Opciones_pedidos.html")

@staff_member_required(login_url='/app-inno-termic/Login/')
def opciones_empleados (req):
    
    return render (req, "Opciones_empleados.html")

@staff_member_required(login_url='/app-inno-termic/Login/')
def opciones_provedores (req):
    
    return render (req, "Opciones_provedores.html")

def sobre_mi (req):
    
    return render (req, "sobre_mi.html")







def cliente_list (req):    
    listar = Cliente.objects.all()
    
    return render (req,"listar_clientes.html", {"lista_clientes": listar} )    

def pedido_list (req):
    listar = Pedido.objects.all()
    
    return render (req,"listar_pedidos.html", {"lista_pedidos": listar} )
    
def empleado_list (req):
    listar = Empleado.objects.all()
    
    return render (req,"listar_empleados.html", {"lista_empleados": listar} )


    




def cliente_detail (req, numero_cliente):
    cliente = get_object_or_404(Cliente, numero_cliente=numero_cliente)
    
    return render(req, 'detalle_cliente.html', {'cliente': cliente})    
    
def pedido_detail (req, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    
    return render(req, 'detalle_pedido.html', {'pedido': pedido})
    
def empleado_detail (req, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    
    return render(req, 'detalle_empleado.html', {'empleado': empleado})






def cliente_create (req):
    if req.method == 'POST':
    
        formClientecreate = ClienteForm(req.POST)
        if formClientecreate.is_valid():
            
            cliente = formClientecreate.cleaned_data
            registro = Cliente(nombre = cliente["nombre"],direccion = cliente["direccion"],telefono = cliente["telefono"],correo_electronico = cliente["correo_electronico"],numero_cliente = cliente["numero_cliente"])
            registro.save()
            return redirect('cliente_detail', numero_cliente= registro.numero_cliente)
    else:        
        formClientecreate = ClienteForm()    
    return render(req, 'crear_cliente.html', {'formClientecreate': formClientecreate})    
    

def pedido_create(req):
    if req.method == 'POST':
        formPedidocreate = PedidoForm(req.POST)
        if formPedidocreate.is_valid():
            pedido = formPedidocreate.save()           
            return redirect('pedido_detail', pk =pedido.pk)
    else:
        formPedidocreate = PedidoForm()

    return render(req, 'crear_pedido.html', {'formPedidocreate': formPedidocreate})

    
def empleado_create (req):
    if req.method == 'POST':
        
        formEmpleado = EmpleadoForm(req.POST)
        if formEmpleado.is_valid():
            empleado = formEmpleado.save()
            return redirect('empelado_detail', pk= empleado.pk)
    else:
        
        formEmpleado = EmpleadoForm()
    
    return render(req, 'crear_empleado.html', {'formEmpleado': formEmpleado})








def cliente_edit(req, numero_cliente):
    cliente = get_object_or_404(Cliente, numero_cliente=numero_cliente)
    
    if req.method == 'POST':
        form = ClienteForm(req.POST)
        if form.is_valid():
            
            cliente.nombre = form.cleaned_data['nombre']
            cliente.direccion = form.cleaned_data['direccion']
            cliente.telefono = form.cleaned_data['telefono']
            cliente.correo_electronico = form.cleaned_data['correo_electronico']
            cliente.numero_cliente = form.cleaned_data['numero_cliente']
            cliente.save()
           
            return redirect('cliente_detail', numero_cliente=cliente.numero_cliente)
    else:
        initial_data = {
            'nombre': cliente.nombre,
            'direccion': cliente.direccion,
            'telefono': cliente.telefono,
            'correo_electronico': cliente.correo_electronico,
            'numero_cliente' : cliente.numero_cliente
        }
        form = ClienteForm(initial=initial_data)
        
    return render(req, 'editar_cliente.html', {'form': form, 'cliente': cliente })

    
def pedido_edit(req, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    
    if req.method == 'POST':
        form = PedidoForm(req.POST, instance=pedido) 
        if form.is_valid():
            
            form.save()
            
            return redirect('pedido_detail', pk=pk)
    else:
       
        form = PedidoForm(instance=pedido)
        
    return render(req, 'editar_pedido.html', {'form': form, 'pedido': pedido })





def empleado_edit (req, pk):
     
    empleado = get_object_or_404(Empleado, pk=pk)
    
    if req.method == 'POST':
       
        form = EmpleadoForm(req.POST, instance=empleado)
        if form.is_valid():
            
            form.save()
            
            return redirect('empelado_detail', pk=pk)
    else:
        
        form = EmpleadoForm(instance=empleado)
    
    return render(req, 'editar_empleado.html', {'form': form, 'empleado': empleado})


    



def cliente_delete (req, numero_cliente):
        
    if req.method == 'POST':
        cliente= Cliente.objects.get(numero_cliente=numero_cliente)
        cliente.delete()        
        return redirect('cliente_list')  
    else: 
        return render(req, 'cliente_delete_confirm.html')

def pedido_delete (req, pk):
        
    if req.method == 'POST':
        pedido= Pedido.objects.get(pk=pk)
        pedido.delete()        
        return redirect('pedido_list')  
    else: 
        return render(req, 'pedido_delete_confirm.html')
    
def empleado_delete (req, pk):
    
    if req.method == 'POST':
        empleado= Empleado.objects.get(pk=pk)
        empleado.delete()        
        return redirect('empleado_list')  
    else: 
        return render(req, 'empleado_delete_confirm.html')
    
    
  
    






    
def pedidos_pendientes (req):
    pedidos_pendientes = Pedido.objects.filter(estado_pedido='pendiente')
    
    return render(req, 'pedidos_pendientes.html', {'pedidos_pendientes': pedidos_pendientes})



    
def resultados_tratamientos (req):
    registros_tratamientos = RegistroTratamiento.objects.all() 
    id_pedido = Pedido.objects.all()

    return render(req, 'resultados_tratamientos.html', {'registros_tratamientos': registros_tratamientos})




def programar_pedido(req):
    if req.method == 'POST':
        form = ProgramacionForm(req.POST)
        if form.is_valid():
            programacion = form.save(commit=False)            
            programacion.save()      
            return redirect('Opciones_provedores')
    else:
        form = ProgramacionForm()

    proveedores_disponibles = Proveedor.objects.all()
    
    return render(req, 'programar_pedido.html', {'form': form})



def registrar_tratamiento(req):
    if req.method == 'POST':
        form = RegistroTratamientoForm(req.POST)
        if form.is_valid():
            registro_tratamiento = form.save()
            
            pedido = registro_tratamiento.pedido_asociado
            pedido.estado_pedido = 'tratado'
            pedido.save()
            return redirect('Opciones_pedidos')
    else:
        form = RegistroTratamientoForm()

    return render(req, 'registrar_tratamiento.html', {'form': form})
    
    
def facturar_pedido(req):
    if req.method == 'POST':
        
        form = FacturaForm(req.POST)
        if form.is_valid():            
            factura = form.save()
            pedido_asociado = factura.pedido_asociado
            pedido_asociado.estado_pedido = 'facturado'
            pedido_asociado.save()
            
            return redirect('Opciones_pedidos')
    else:
        form = FacturaForm()

    return render(req, 'facturar_pedido.html', {'form': form})



def crear_documento(req, pk):
    cliente = get_object_or_404(Cliente, numero_cliente=pk)

    if req.method == 'POST':
        
        form = DocumentoForm(cliente, req.POST)
        if form.is_valid():            
            documento = form.save(commit=False)
            documento.save()
            return redirect('cliente_detail', numero_cliente=pk)
    else:
        form = DocumentoForm(cliente)

    return render(req, 'crear_documento.html', {'form': form, 'cliente': cliente})


def ver_certificado(req, pk):
    cliente = get_object_or_404(Cliente, numero_cliente=pk)
    pedidos_del_cliente = Pedido.objects.filter(cliente=cliente)    
    certificados = Documento.objects.filter(asociado_pedido__in=pedidos_del_cliente)
    
    return render(req, 'ver_certificados.html', {'cliente': cliente, 'certificados': certificados})


def registrar_resultado_calidad(req):
    if req.method == 'POST':
        
        form = RegistroCalidadForm(req.POST)
        if form.is_valid():
            
            registro_calidad = form.save(commit=False)
            registro_calidad.responsable_prueba = req.user
            registro_calidad.save()
                       
            return redirect('Opciones_pedidos')
    else:
        form = RegistroCalidadForm()

    return render(req, 'registrar_resultado_calidad.html', {'form': form})


    
def listar_capacitaciones (req,empleado_id):
    empleado = Empleado.objects.get(pk=empleado_id)
    capacitaciones_empleado = empleado.capacitaciones.all()    
    
    return render(req, 'listar_capacitacion.html', {'capacitaciones_empleado': capacitaciones_empleado, 'empleado': empleado})


def detalle_capacitacion_empleado(request, capacitacion_id, empelado_id):
    capacitacion = get_object_or_404(Capacitacion, pk=capacitacion_id)
    empleado =get_object_or_404(Empleado, pk = empelado_id)
      
    return render(request, 'detalle_capacitacion_empleado.html' ,{ 'capacitacion': capacitacion , 'empleado': empleado })


def crear_capacitacion(req):
    if req.method == 'POST':
        
        form = CapacitacionForm(req.POST)
        if form.is_valid():
            capacitacion = form.save()
            
            return redirect('empleado_create') 
    else:
        form = CapacitacionForm()
    
    return render(req, 'crear_capacitacion.html', {'form': form})


class ServiciosList(ListView):
    model= ServicioTratamiento
    template_name= "lista_servicios.html"
    context_object_name = "servicio"
    
    

class ServiciosDetail(DetailView):
    model = ServicioTratamiento
    template_name = "detalle_servicios.html"
    context_object_name = "servicio"
    
    
    
    
    
    
    
    
    
def login_user (req):
    if req.method== 'POST':
        form = AuthenticationForm(req, data=req.POST)
        if form.is_valid():
            data = form.cleaned_data
            usuario = data["username"]
            password = data["password"]
            user = authenticate(username=usuario, password = password)
            
            if user:
                login(req, user)
                return render(req, 'inicio.html', {'mensaje': f'Bienvenido {usuario}'})
        return render(req, 'inicio.html', {'mensaje': f'Datos incorrectos'})
            
    else:
        form = AuthenticationForm()
        return render(req, 'login.html', {'form': form})
            


def register_user (req):
    if req.method== 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            usuario = data["username"]
            form.save()
            return render(req, 'inicio.html', {'mensaje': f'Usuario {usuario} creado con exito!'})
        return render(req, 'inicio.html', {'mensaje': f'formulario invalido'})
        
            
    else:
        form = UserCreationForm()
        return render(req, 'register.html', {'form': form})
    
    
    
def crear_servicio(req):
    if req.method == 'POST':
        form = ServicioTratamientoForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_servicio')
    else:
        form = ServicioTratamientoForm()
    
    return render(req, 'crear_servicio.html', {'form': form})


def listar_servicio (req):    
    listar_servicio = ServicioTratamiento.objects.all()
    
    return render (req,"listar_servicios.html", {"listar_servicio": listar_servicio} )


def detalle_servicio (req, numero_servicio):
    servicio = get_object_or_404(ServicioTratamiento, pk =numero_servicio)
    
    return render(req, 'detalle_servicio.html', {'servicio': servicio})


def contacto(req):
    if req.method == 'POST':
        nombre = req.POST.get('nombre')
        email = req.POST.get('email')
        mensaje = req.POST.get('mensaje')

        asunto = 'Mensaje de contacto de {}'.format(nombre)
        remitente = settings.DEFAULT_FROM_EMAIL
        destinatario = ['innovacion.termica@gmail.com']

        mensaje_email = render_to_string('datos_contacto.html', {
            'nombre': nombre,
            'email': email,
            'mensaje': mensaje,
        })
        email_message = EmailMessage(asunto, mensaje_email, remitente, destinatario)
        email_message.content_subtype = 'html'

        try:
            email_message.send()
            return render(req, 'confirmacion_email.html')
           
        except Exception as e:
            return render(req, 'error_email.html')

    return render(req, 'contacto.html')


@login_required
def edit_user(req):
    if req.method == 'POST':
        form = UserEditForm(req.POST, instance=req.user)
        if form.is_valid():
            user = form.save(commit=False)
            password1 = form.cleaned_data.get('password1')
            if password1:
                user.set_password(password1)
                update_session_auth_hash(req, user)  # Actualiza la sesión del usuario
            user.save()
            return render(req, 'inicio.html', {'mensaje': 'Datos modificados correctamente'})
        else:
            return render(req, 'edit_user.html', {'form': form})
            
    else:
        form = UserEditForm(instance=req.user)

    return render(req, 'edit_user.html', {'form': form})


@login_required


def agregar_avatar(req):
    usuario = req.user
    try:
        avatar_existente = Avatar.objects.get(user=usuario)
    except Avatar.DoesNotExist:
        avatar_existente = None

    if req.method == 'POST':
        form = AvatarForms(req.POST, req.FILES)
        if form.is_valid():
            data = form.cleaned_data
            if avatar_existente:
                # Si el usuario ya tiene un avatar, actualiza el avatar existente
                avatar_existente.imagen = data["imagen"]
                avatar_existente.save()
            else:
                # Si el usuario no tiene un avatar, crea uno nuevo
                nuevo_avatar = Avatar(user=usuario, imagen=data["imagen"])
                nuevo_avatar.save()

            return render(req, 'inicio.html', {'mensaje': 'Avatar agregado/modificado correctamente'})
    else:
        # Si el usuario ya tiene un avatar, muestra el formulario de edición
        if avatar_existente:
            form = AvatarForms(instance=avatar_existente)
        else:
            form = AvatarForms()

    return render(req, 'agregar_avatar.html', {'form': form})



#def agregar_avatar(req):
    if req.method == 'POST':
        form = AvatarForms(req.POST, req.FILES)
        if form.is_valid():
            data = form.cleaned_data
            avatar = Avatar(user=req.user, imagen =data["imagen"])
            avatar.save()
           
            return render(req, 'inicio.html', {'mensaje': 'Avatar agregado correctamente'})
        else:
            return render(req, 'edit_user.html', {'form': form})
            
    else:
        form = AvatarForms()

        return render(req, 'agregar_avatar.html', {'form': form})