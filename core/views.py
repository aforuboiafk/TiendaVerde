from django.shortcuts import render

# Create your views here.
def home(request):
    titulo = "Inicio"
    data = {
        "titulo": titulo
    }
    return render(request,'core/base.html', data)


def productos(request):
    titulo = "Inicio"
    data = {
        "titulo": titulo
    }
    return render(request,'core/productos.html', data)


def carrito(request):
    titulo = "Inicio"
    data = {
        "titulo": titulo
    }
    return render(request,'core/carrito.html', data)
def cuenta(request):
    titulo = "Inicio"
    data = {
        "titulo": titulo
    }
    return render(request,'core/cuenta.html', data)
def login(request):
    titulo = "Inicio"
    data = {
        "titulo": titulo
    }
    return render(request,'core/login.html', data)