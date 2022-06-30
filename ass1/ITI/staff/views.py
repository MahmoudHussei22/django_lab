from django.test import TestCase

# Create your tests here.
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse , HttpResponseRedirect

# Create your views here.
def index(reques):
    return HttpResponse('Hello World')

def insert(req):
    return JsonResponse({"name": "Ahmed"})

def update(re):
    return JsonResponse({"name": "Ahmed"})

def deleer(reqs):
    return HttpResponseRedirect('insertUser.html')


