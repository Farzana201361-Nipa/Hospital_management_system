from django.shortcuts import render, HttpResponse
from . import urls

# Create your views here.

def home(request):
    return render(request, 'base.html')
