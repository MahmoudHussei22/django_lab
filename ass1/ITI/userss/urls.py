from django.test import TestCase

# Create your tests here.
from django.contrib import admin
from django.urls import path,include
from .views import *
from userss.views import *
from trainee.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('indexHome/',Homeview),
    path('',Login,name='Login'),
    path('logout/',logout,name='logout'),
    path('Register/',Register,name='Register'),
    path('Login/',Login,name='Login'),
    path('Users/',Users,name='users'),
    path('send/',sendUser,name='send'),

]