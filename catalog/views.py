from django.shortcuts import render
from .models import *
# Create your views here.
def index(req):
    numkino = Kino.objects.all().count()
    numacter = Actor.objects.all().count()
    numfree = Kino.objects.filter(status__kino=1).count()
    data = {'k1':numkino,'k2':numacter,'k3':numfree}
    return render(req,'index.html', context=data)

#def allkino(req):
   # return render(req, 'index.html')

from django.views import generic
class Kinolist123(generic.ListView):
    model = Kino


class KinoDetail(generic.DetailView):
    model = Kino

#from django.http import HttpResponse
#def info(req,id):
    #film = Kino.objects.get(id=id)
    #return HttpResponse(film.title)

