from django.shortcuts import render
from afisha.models import Carousel

# Create your views here.

def afisha_view(request):
    afisha = Carousel.objects.all()
    context_dict={'afisha':afisha}
    return render (request, 'afisha/afisha.html', context_dict)

