from django.test import TestCase

# Create your tests here.
from django.urls import path
from .views import *

urlpatterns = [
path('',listuser),
path('Update/<id>/',Update,name='updateuser'),
path('send/',send,name='senduser'),
path('courses/<id>/',get_courses,name='courses'),

path('add_courses/<id>/',add_courses,name='add_courses'),
path('Delete/<id>/',Delete,name='deleteuser'),
]