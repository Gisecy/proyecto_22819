from django.http import HttpResponse
from django.shortcuts import HttpResponse, render

# Create your views here.
def hola_mundo(request):
    return HttpResponse("Hola mundo Django")
    