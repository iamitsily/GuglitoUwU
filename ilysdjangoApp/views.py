from django.http import HttpResponse
def home(request):
    return HttpResponse("ola a todos amigos de django")
def yahir(request):
    return HttpResponse(request, 'templatesyahir.html')