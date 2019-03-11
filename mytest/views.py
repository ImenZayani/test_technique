from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import Equipe, Joueur
from .serializers import EquipeSerializer, JoueurSerializer
from rest_framework import permissions
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.forms import ModelForm

# Create your views here.


class EquipeViewSet(viewsets.ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer


class EquipeForm(ModelForm):
    class Meta:
        model = Equipe
        fields = ['nom', 'drapeau']

def equipe_list(request, equipes='equipes/equipes_list.html'):
    equipe = Equipe.objects.all()
    data = {}
    data['object_list'] = equipe
    return render(request, equipes, data)


def equipe_view(request, id, equipes='equipes/equipes_detail.html'):
    equipe= get_object_or_404(Equipe, id=id)    
    return render(request, equipes, {'object':equipe})

def equipe_create(request, equipes='equipes/equipes_form.html'):
    form = EquipeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('equipe_list')
    return render(request, equipes, {'form':form})


def equipe_update(request, id, equipes='equipes/equipes_form.html'):
    equipe= get_object_or_404(Equipe, id=id)
    form = EquipeForm(request.POST or None, instance=equipe)
    if form.is_valid():
        form.save()
        return redirect('equipe_list')
    return render(request, equipes, {'form':form})






class JoueurViewSet(viewsets.ModelViewSet):
    queryset = Joueur.objects.all()
    serializer_class = JoueurSerializer
    def get_queryset(self):
         return Joueur.objects.filter(equipe_id=self.kwargs['equipe_id'])

class JoueurForm(ModelForm):
    class Meta:
        model = Joueur
        fields = ['nom', 'num' , 'present' , 'equipe_id']

def joueur_list(request, joueurs='joueurs/joueurs_list.html'):
    joueur = Joueur.objects.all()
    data = {}
    data['object_list'] = joueur
    return render(request, joueurs, data)


def joueur_view(request, id, joueurs='joueurs/joueurs_detail.html'):
    joueur= get_object_or_404(Equipe, id=id)    
    return render(request, joueurs, {'object':joueur})

def joueur_create(request, joueurs='joueurs/joueurs_form.html'):
    form = JoueurForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('joueur_list')
    return render(request, joueurs, {'form':form})


def joueur_update(request, id, joueurs='joueurs/joueurs_form.html'):
    joueur= get_object_or_404(Joueur, id=id)
    form = JoueurForm(request.POST or None, instance=joueur)
    if form.is_valid():
        form.save()
        return redirect('joueur_list')
    return render(request, joueurs, {'form':form})

 


