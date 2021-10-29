from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>HOLA MUNDO</h1>")

def nosotros(request):
    return HttpResponse("<h1>SOMOS NOSOTROS</h1>")
