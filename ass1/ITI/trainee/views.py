from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from student.models import *
# Create your views here.
def listuser(req):
    users=MyUser.objects.all()
    context={}
    context['users']=users
    return render(req,'list.html',context)
def send(req):
    if (req.method == 'GET'):
  from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from student.models import *
# Create your views here.
def listuser(req):
    users=MyUser.objects.all()
    context={}
    context['users']=users
    return render(req,'list.html',context)
def send(req):
    if (req.method == 'GET'):
        return render(req, 'insertUser.html')
    else:
        u = userss(username=req.POST['username'])
        u.email = req.POST['email']
        u.password = req.POST['password']
        u.save()
        return render(req, 'tem.html')

def Update(req,id):
    if(req.session.get('username') is not None):
        context={}
        if(req.method=='GET'):
            context['user']=MyUser.objects.get(id=id)
            return render(req, 'update.html', context)
        else:
            MyUser.objects.filter(id=id).update(username=req.POST['username'],email=req.POST['username'])
            return HttpResponseRedirect('/User/Users/')#render(req, 'myuser/list.html', context)
    else:
        return HttpResponseRedirect('/')

def get_courses(req, id):
    if(req.session.get('username') is not None):
        context={}
        if(req.method=='GET'):
            req.session.courses = courses.objects.filter(user__id=id)

            return render(req, 'courses.html')
        else:
            return HttpResponseRedirect('/User/Users/')#render(req, 'myuser/list.html', context)
    else:
        return HttpResponseRedirect('/')

def add_courses(req, id):
    if(req.session.get('username') is not None):
        context={}
        if(req.method=='GET'):
            return render(req, 'addCourses.html')
        else:
            user = MyUser.objects.get(id=id)
            course = courses(user=user, name=req.POST['name'])
            course.save()
            return HttpResponseRedirect('/User/Users/')#render(req, 'myuser/list.html', context)
    else:
        return HttpResponseRedirect('/')

def Delete(req,id):
    if(req.session.get('username') is not None):
        x=MyUser.objects.filter(id=id).delete()
        return HttpResponseRedirect('/User/Users/')
    else:
        return HttpResponseRedirect('/')
