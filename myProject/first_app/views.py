from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    diccionario = {'nombres':"Luis Enrique"}
    return render(request,'first_app/index.html',context=diccionario)

def prueba(request):
    return render(request,'first_app/prueba.html')
