from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if(request.method=="GET"):
        titulo = "Titulo cuando se accede por GET modificado"
    else:
        titulo = f'Titulo cuando se accede por otro metodo{request.method}'
    parameters_get =request.GET.get('algo')
    #return HttpResponse(f"""
    #    <h1>{titulo}</h1>
    #    <p>{parameters_get}</p>
    # """)
    listado_cursos= {
        "nombre": "Fullstack Java",
        "descripcion": "Curso de Fullstack",
        "categoria": "Programación"
    },
    {
        "nombre": "Diseño UX/IU",
        "descripcion": "",
        "categoria": "Diseño"
    },
    {
        "nombre": "",
        "descripcion": "",
        "categoria": "Programación"
    },
    return render(request,'cac/index.html', {'titulo': titulo})

def hola_mundo(request):    
    return HttpResponse("Hola mundo Django")

def saludar(request, nombre='Pepe'):
    return HttpResponse(f"""
        <h1>Hola Mundo Django - {nombre}</h1>
        <p>Estoy haciendo mi primera prueba</p>
    """)
    
def ver_proyectos(request, anio, mes=1):
    return HttpResponse(f"""
        <h1>Proyectos del - {mes}/{anio}</h1>
        <p>Listado de Proyectos</p>
    """)
    
def cursos_detalle(request, nombre_curso):
    return HttpResponse(f"""
        <h1>{nombre_curso}</h1>
    """)

def cursos(request, nombre):
    return HttpResponse(f"""
        <h1>{nombre}</h1>
    """)  
    
def ver_proyecto_anio(request, anio):
    return HttpResponse(f"""
        <h1>Proyectos del {anio}</h1>
        <p>Listado de Proyectos</p>
    """)

def ver_proyecto_2022_07(request):
    return HttpResponse(f"""
        <h1>Proyectos del mes 7 del año 2022</h1>
        <p>Listado de Proyectos</p>
    """)
    
def quienes_somos(request):
    #return redirect("saludar_por_defecto")
    return redirect(reverse("saludar", kwargs={'nombre': "Gisela"}))
    pass

