from django.test import TestCase

# Create your tests here.
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse

# Create your views here.
def liststu(r):
    return HttpResponse('liststudeint')

def liststaff(re):
    return HttpResponse('liststaff')

def main(req):
    return HttpResponse('links')
