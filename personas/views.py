

from sqlite3 import DateFromTicks
from django.http import HttpResponse
from django.shortcuts import render
from requests import delete
from personas.models import Amigos, Familiares,Clientes
from django.http import HttpResponse
from personas.forms import Alta_Amigos, Alta_Familiar, Alta_Clientes
##import datetime
# Create your views here.


def inicio(request):

    return render( request , "index.html")

def lista_amigos(request):

    amigos = Amigos.objects.all() ## pedido a la base de datos de todo
    datos = { "datos" : amigos}

    return render( request, "lista_amigos.html" , datos)

def lista_familiares(request):

    familiar = Familiares.objects.all() ## pedido a la base de datos de todo
    datos = { "datos" : familiar}

    return render( request, "lista_familiares.html" , datos)  

def lista_clientes(request):

    cliente = Clientes.objects.all() ## pedido a la base de datos de todo
    datos = { "datos" : cliente}

    return render( request, "lista_clientes.html" , datos)     

def alta_familiar(request):

    if request.method =="POST":

            formulario = Alta_Familiar( request.POST )

            if formulario.is_valid():
                
                datos = formulario.cleaned_data  ## datos del formulario limpios
                dato = Familiares( nombre=datos[ 'nombre' ] , edad=datos[ 'edad' ]) ## llamo a la clase familiares 
                dato.save() 
                
                familiares = Familiares.objects.all() ## pedido a la base de datos de todo
                datos = { "datos" : familiares}
                
                return render(request , "lista_familiares.html" , datos)
            
    return render(request , "alta_familiar.html")  #agregar html de error
    
def alta_amigos(request):

    if request.method =="POST":

            formulario = Alta_Amigos( request.POST )

            if formulario.is_valid():
                
                datos = formulario.cleaned_data  ## datos del formulario limpios
                dato = Amigos( nombre=datos[ 'nombre' ] , edad=datos[ 'edad' ]) ## llamo a la clase familiares 
                dato.save() 
                
                amigos = Amigos.objects.all() ## pedido a la base de datos de todo
                datos = { "datos" : amigos}
                
                return render(request , "lista_amigos.html" , datos)
            
    return render(request , "alta_amigos.html")  #agregar html de error

def alta_clientes(request):

    if request.method =="POST":

            formulario = Alta_Clientes( request.POST )

            if formulario.is_valid():
                
                datos = formulario.cleaned_data  ## datos del formulario limpios
                dato = Clientes( nombre=datos[ 'nombre' ] , edad=datos[ 'edad' ]) ## llamo a la clase familiares 
                dato.save() 
                
                cliente = Clientes.objects.all() ## pedido a la base de datos de todo
                datos = { "datos" : cliente}
                
                return render(request , "lista_clientes.html" , datos)
            
    return render(request , "alta_clientes.html")  #agregar html de error

def busqueda(request):

    return render( request , "formulario_busqueda.html")


def buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        familiar = Familiares.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busqueda.html" , {"familiar": familiar})
    
    elif request.GET['nombre']:
        nombre = request.GET['nombre']
        amigo = Amigos.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busqueda.html" , {"amigo": amigo})    

    else:

        return HttpResponse(f" no se encontro")



def eliminar_familiar(request , id): 

    familiar = Familiares.objets.get( id = id)
    familiar.delete()

    familiar = Familiares.objects.all()

    return render(request , "lista_familiares.html" ,  {"familiar" : familiar})
"""

def editar_familiar(request , id):

    familiar = familiares.objects.get( id = id )

    if request.method == "POST":

        mi_formulario = Familiar_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data   ## me devuelve un diccionario limpio
            familiar.nombre = datos["nombre"]
            familiar.edad = datos["edad"]
            familiar.save()

            return HttpResponse(" Editado ")
            #return render(request , ".html" , {"cursos": curso}) en mi caso familiares
    else:

        mi_formulario = Familiar_formulario(initial={"nombre" : familiar.nombre , "edad": familiar.edad })

    return render(request , "editar_formulario" , {"mi_formulario":mi_formulario})    
    
"""