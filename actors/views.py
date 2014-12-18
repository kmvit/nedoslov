from django.shortcuts import render, get_object_or_404
from actors.models import Actors

# Create your views here.

def actors(request):
    actors = Actors.objects.all()
    context_dict = {'actors':actors}
    return render (request, 'actors/actors.html', context_dict)


def actor_view(request,slug):
    actor=get_object_or_404(Actors, slug=slug),
    context_dict = {'actor':actor}
    
    return render(request, 'actors/actor_detail.html', context_dict)
