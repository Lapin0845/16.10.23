from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User, Group
# Create your views here.
def index(req):
    numkino = Kino.objects.all().count()
    numacter = Actor.objects.all().count()
    numfree = Kino.objects.filter(status__kino=1).count()
    if req.user.username:
        username = req.user.first_name
        print(req.user.first_name,'#',req.user.id)
    else:
        username = 'Гость'
        print(req.user.id)
    data = {'k1':numkino,'k2':numacter,'k3':numfree}
    #user = User.objects.create('User2','user2gmail.ru','useruser')
    #user.first_name = "Vlad"
    #user.last_name = 'Petrov'
    return render(req,'index.html', context=data)

#def allkino(req):
   # return render(req, 'index.html')

from django.views import generic
class Kinolist123(generic.ListView):
    model = Kino


class KinoDetail(generic.DetailView):
    model = Kino


class Actorlist(generic.ListView):
    model = Actor

class Directorlist(generic.ListView):
    model = Director

#from django.http import HttpResponse
#def info(req,id):
    #film = Kino.objects.get(id=id)
    #return HttpResponse(film.title)

def status(req):
    k1 = Status.objects.all()
    data ={'podpiska':k1}
    return render(req, 'podpiska.html', context=data)

def prosmotr(req,id1,id2,id3):
    print(id1,id2,id3)
    mas =['бесплатно','базовая','супер']
    mas2 =['free','based','super']
    status=0
    if id3!=0:
        status = User.objects.get(id=id3)
        print(status)
        status = status.groups.all()
        print(status)
        status = status[0].id
        print(status)
    else:
        if id3==0:
            status=1
        if status>=id2:
            print('ok')
            permission = True
        else:
            print('nelza')
            permission = False
        k1 = Kino.objects.get(id=id1).title
        k2 = Group.objects.get(id=status).name
        k3 = Status.objects.get(id=id2).name
        data = {'kino':k1, 'status':k2, 'statusakino':k3, 'prava':permission}
        return render(req,'prosmotr.html',data)

def buy(req,type):
    usid = req.user.id
    user123 = User.objects.get(id=usid)
    statusnow = user123.groups.all()[0].id
    grold = Group.objects.get(id=statusnow)
    grold.user_set.remove(user123)
    grnew = Group.objects.get(id=type)
    grnew.user_set.add(user123)
    k1 = grnew.name
    data = {'podpiska':k1}
    return render(req,'buy',data)

from .form import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
def registr(req):
    print(1)
    if req.POST:
        print(2)
        anketa = SignUpForm(req.POST)
        if anketa.is_valid():
            print(3)
            anketa.save()
            k1 = anketa.cleaned_data.get('username')
            k2 = anketa.cleaned_data.get('password1')
            k3 = anketa.cleaned_data.get('first_name')
            k4 = anketa.cleaned_data.get('last_name')
            k5 = anketa.cleaned_data.get('email')
            user = authenticate(username=k1, password=k2)#сохраняет нового пользователя
            man = User.objects.get(username=k1)#находим нового юзера
            man.email=k5
            man.first_name=k3
            man.last_name=k4
            man.save()
            login(req,user)    #входит на сайт
            group = Group.objects.get(id=1)#находим бесплатную подписку
            group.user_set.add(man)       #записываем юзера в подписку
            return redirect('home')
    else:
        anketa = SignUpForm()
    data={'regform':anketa}
    return render(req,'registration/registration.html',context=data)