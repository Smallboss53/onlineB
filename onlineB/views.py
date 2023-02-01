from django.shortcuts import render
from .models import Scenary

def home(request):

    dests = Scenary.objects.all()
    return render (request,"home.html", {'dests':dests})
