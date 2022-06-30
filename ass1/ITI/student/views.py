from django.test import TestCase

# Create your tests here.
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse

# Create your views here.
def listt(reques):
    return HttpResponse('list')

def insert(req):
    return render( req , 'insertUser.html')

def insert(req):
    return render( req , 'insertUser.html')
