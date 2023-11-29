from django.http import HttpResponse
from django.template import Template, Context
def home(request):
    return HttpResponse("ola a todos amigos de django")
def yahir(request):
    doc_externo = open("Y:/Github/ISINTAXIS/GuglitoUwU/ilysdjangoApp/templates/Guglitouwu/yahir.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)