from django.shortcuts import render
from student.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as  authlogin,logout as authlogout

def Homeview(req):
    if (req.session.get('username') is None):
        return render(req,'indexx.html',{'viewname':'Home'})
    else:
        return render(req, 'loginn.html')

def Register(req):
    if(req.method=='GET'):
        return render(req,'registerTemp.html')
    elsfrom django.shortcuts import render
from student.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as  authlogin,logout as authlogout

def Homeview(req):
    if (req.session.get('username') is None):
        return render(req,'indexx.html',{'viewname':'Home'})
    else:
        return render(req, 'loginn.html')

def Register(req):
    if(req.method=='GET'):
        return render(req,'registerTemp.html')
    else:
        MyUser.objects.create(username=req.POST['username'],email=req.POST['email'],password=req.POST['password'])
        #redirect to login
        #change url
        return render(req, 'loginTemp.html')

def Login(req):
    req.session.clear()
    if (req.session.get('username') is None):
        if (req.method == 'GET'):
            return render(req, 'loginTemp.html')
        else:
            # check user cred in myuser
            myuserobject = MyUser.objects.filter(username=req.POST['username'], password=req.POST['password'])
            print(myuserobject)
            # check user cred in authuser
            authuserobject = authenticate(username=req.POST['username'], password=req.POST['password'])
            if (len(myuserobject) > 0):
                print('ooooooooooooooooooooo')
                req.session['username'] = myuserobject[0].username
                # authlogin(req, authuserobject)
                req.session.users=MyUser.objects.all()
                return render(req, 'tem.html')

            else:
                print('errrrro')
                context = {}
                context['error'] = 'invalid cred.'

                return render(req, 'loginTemp.html', context)
    else:
        return render(req, 'loginTemp.html')
    # else:
    #     print('errrrror')
    #     context = {}
    #     context['error'] = 'invalid cred.'
    #     return render(req, 'loginn.html', context)

def logout(req):
    req.session.clear()
    authlogout(req)
    return render(req,'loginTemp.html')


def Users(req):
    # req.session.clear()
    req.session.users=MyUser.objects.all()
    return render(req, 'indexx.html')

def sendUser(req):
    if (req.method == 'GET'):
        return render(req, 'insertUserForm.html')
    else:
        MyUser.objects.create(username=req.POST['username'],email=req.POST['email'],password=req.POST['password'])
        return render(req, 'insertUserForm.html')