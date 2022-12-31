from re import template
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import joblib

def index(request):
    template=loader.get_template("index.html")
    return HttpResponse(template.render())


def logement(request):
    template = loader.get_template("mcln.html")
    return HttpResponse(template.render({},request))

def predire(request):
    if request.method =='POST':
        niv_classe=int(request.POST['niv_classe'])
        servent=int(request.POST['servent'])
        dejeune=int(request.POST['dejeune'])
        soupe=int(request.POST['soupe'])
        nbr_sejours=int(request.POST['nbr_sejours'])

        tableau=[[niv_classe,servent,dejeune,soupe,nbr_sejours]]
        
        regresseur=joblib.load('modele_mcln/notreModel.pkl')
        print(tableau)

    return HttpResponse(regresseur.predict(tableau))
