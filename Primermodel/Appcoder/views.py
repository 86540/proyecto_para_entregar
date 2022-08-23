from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
def amigos(self):
    amigos= amigos(nombres="Manuel y Gianfranco")
    amigos.save()
    variable=(f"{amigos} son mis mejores amigos")
    return HTTPResponse(variable)
