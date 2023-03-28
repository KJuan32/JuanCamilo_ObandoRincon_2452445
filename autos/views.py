from django.shortcuts import render
from django.http import HttpResponse



def autos(request):
    auto=['TOYOTA', 'MCLAREN','FERRARI']
    context={'listado':auto}
    return render(request, 'autos.html', context)

def clientes(request):
    clientes=['Juan Camilo', 'Daniela Salazar', 'Danilo Dagua']
    context={'listado':clientes}
    return render(request, 'clientes.html', context)

