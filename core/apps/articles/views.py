from django.http import HttpResponse


# Create your views here.
def homepage(request):
    return HttpResponse('This is our homepage! It works!')
