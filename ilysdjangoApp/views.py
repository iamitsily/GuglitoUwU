import os
from django.http import HttpResponse, JsonResponse
from django.template import Template, Context
def home(request):
    return HttpResponse("ola a todos amigos de django")
def guglito(request):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta_doc_externo = os.path.join(BASE_DIR, 'ilysdjangoApp', 'templates', 'Guglitouwu', 'guglito.html')


    doc_externo = open(ruta_doc_externo)
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)

    return HttpResponse(documento)

def buscarPalabra(palabra):
    respuesta_json = buscadorURLS.buscar_palabra(palabra )
    return JsonResponse(respuesta_json)