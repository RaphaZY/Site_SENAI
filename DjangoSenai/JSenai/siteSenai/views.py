from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.

def index(request):
    card = Cards.objects.all()
    return render(request,"site/index.html", {'info':card})

def cadcard(request):
    form = CardsForm
    if request.method == "POST":
        form = CardsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        
        return redirect("index")

    return render(request, "site/ccard.html", {"form": form})


def caduser(request):
    form = UsuariosForms
    if request.method == "POST":
        form = UsuariosForms(request.POST)
        if form.is_valid():
            form.save()

    user = Usuarios.objects.all()

    return render(request, "site/cuser.html", {'users':user, "form": form})