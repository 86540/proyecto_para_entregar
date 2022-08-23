from contextvars import Context
from multiprocessing import context
from pipes import Template
from django.http import HttpResponse
from django.template import Template, Context

def nombre(request):
    return HttpResponse ("Mi hermana se llama Sonia")

def primertemplate(self):
    nombres_de_mi_familia="David","Sonia","Norma","Jose"
    diccionario={"los nombres de mi familia son": nombres_de_mi_familia}
    mihtml= open("C:/Users/alejo/Desktop/proyecto1/proyectoentregable/proyectoentregable/plantillas")
    plantilla=Template(mihtml.read())
    mihtml.close()
    mi_contexto=Context(diccionario)
    documento=plantilla.render(mi_contexto)

    return HttpResponse(documento)
    