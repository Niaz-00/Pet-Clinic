from django.shortcuts import render
from .models import Vets


# Create your views here.

def home(request):

    context = {
        "name": "Home"
    }

    return render(request, 'index.html', context)


def vets(request):
    obj = Vets.objects.get(id=1)

    context = {
        "data": obj
    }

    return render(request, 'vets/vets.html', context)
