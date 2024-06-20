from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipe/pages/home.html')


def contato(request):
    return HttpResponse("<h1>Contato Page</h1>")


