from django.shortcuts import render, HttpResponse
from . import urls

# Create your views here.

def home(request):
    return HttpResponse ("<h1> xyz</h1> ")
