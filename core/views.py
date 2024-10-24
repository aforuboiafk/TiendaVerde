from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import Carro, Producto


# Create your views here.
def home(request):
    titulo = "Inicio"
    data = {
        'titulo' : "Bienvenido a Mi Tienda",
        'subtitulo' : "Los mejores productos al mejor precio",
        'descripcion_izquierda' : "Explora nuestra amplia gama de productos diseñados para satisfacer tus necesidades.",
        'descripcion_derecha' : "Disfruta de descuentos exclusivos y ofertas increíbles solo para nuestros clientes.",
        'boton_texto' : "Ver Productos"
    }
    return render(request,'core/landing.html', data)


def productos(request):
    productos = Producto.objects.all()  # Obtener todos los productos de la base de datos
    data = {
        "productos": productos
    }
    return render(request, 'core/productos.html',data)


def carrito(request):
    titulo = "Inicio"
    data = {
        "titulo": titulo
    }
    return render(request,'core/carrito.html', data)


def cuenta(request):
    titulo = "Inicio"
    data = {
        'usuario' : request.user
    }
    return render(request,'core/cuenta.html', data)


def inicio_sesion(request):
    titulo = "Inicio"
    data = {
        "titulo": titulo
    }

    #OBTENEMOS LOS DATOS
    if request.method == 'POST':
        usuario = request.POST['usuario']
        contraseña = request.POST['contraseña']

        usuario_final = User.objects.filter(username=usuario).first()
        
        if not usuario_final:
            messages.error(request, "El usuario no existe")
            return render(request,'core/login.html')


        if usuario_final.check_password(contraseña):    
            login(request, usuario_final)
            print(usuario_final)
            print('todo weno')
            return redirect('/')
        
        else:
            messages.error(request,"El usuario no existe")
            return render(request,'core/login.html')

    return render(request,'core/login.html', data)


def register(request):
    titulo = "Inicio"
    data = {
        "titulo": titulo
    }
#   OBTENEMOS LOS DATOS
    if request.method == 'POST':
        usuario = request.POST['usuario']
        email = request.POST['email']
        contraseña1 = request.POST['contraseña1']
        contraseña2 = request.POST['contraseña2']
        
        print(contraseña1)
        print(contraseña2)


        if contraseña1 != contraseña2:
            messages.error(request, "Las contraseñas no coinciden")
            return render(request, 'core/registro.html')
        
        if User.objects.filter(username=usuario).exists():
            messages.error(request, "El usuario ya existe")
            return render(request, 'core/registro.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "El email ya existe")
            return render(request, 'core/registro.html')
        
        usuario_final = User.objects.create_user(username=usuario, email=email,password=contraseña1)
        
        usuario_final.save()

        login(request, usuario_final)
        print(usuario_final)
        return redirect('/')
        
    return render(request,'core/registro.html', data)


def cerrar_sesion(request):
    logout(request)
    return redirect('/')