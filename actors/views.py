from django.shortcuts import render
from actors.models import Actors

# Create your views here.

def actors(request):
    actors = Actors.objects.all()
    context_dict = {'actors':actors}
    return render (request, 'actors/actors.html', context_dict)
