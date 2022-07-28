from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render


def fecha_actual(request):
    fecha = datetime.now().date()
    mensaje = f'Hoy es {fecha}'
    return HttpResponse(mensaje)
