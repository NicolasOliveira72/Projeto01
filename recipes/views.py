# from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('F. 451 - Ray B.')

def contato(request):
    return HttpResponse('contato2')

def sobre(request):
    return HttpResponse('sobre2')
