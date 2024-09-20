from django.http import HttpResponse # type: ignore

def index(request):
    return HttpResponse("Hello World, we're making a polls website")
