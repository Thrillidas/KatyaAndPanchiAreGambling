from django.shortcuts import render
from django.http import HttpResponse
from django import forms
# Create your views here.

apuestas = []

class NewGambleForm(forms.Form):
    apuesta = forms.CharField(label="New Bet")

def index(request):
    return render(request, "Gambling/index.html", {
        "apuestas": apuestas
    })

def add (request):
    if request.method == "POST":
        form = NewGambleForm(request.POST)
        if form.is_valid():
            apuesta = form.cleaned_data["apuesta"]
            apuestas.append(apuesta)
        else:
            return render(request, "Gambling/add.html" , {
                "form": form
            })


    return render(request, "Gambling/add.html", {
        "form": NewGambleForm()
    })
    