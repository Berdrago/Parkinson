from django.shortcuts import render

from parkinson.forms import formAgregar
from parkinson.models import Creacion_modulo_MBM

# Create your views here.

def index(request):
    return render(request,"index.html")
def elements(request):
    return render(request,"elements.html")
def generic(request):
    return render(request,"generic.html")
def formulario(request):
    creacionmodulo =  Creacion_modulo_MBM.objects.filter().order_by('-id_mbm') 
    contexto=  {
        'creacionmodulos':creacionmodulo}

    return render(request,"formulario.html", contexto)

