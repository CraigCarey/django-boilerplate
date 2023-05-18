from django.http import HttpResponse


def index(request):
    return HttpResponse("Hula, world. You're at the accounts index.")
