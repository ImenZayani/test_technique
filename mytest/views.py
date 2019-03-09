from django.shortcuts import render
from rest_framework import viewsets
from .models import Equipe, Joueur
from .serializers import EquipeSerializer, JoueurSerializer
from rest_framework import permissions


# Create your views here.


class EquipeViewSet(viewsets.ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer

class JoueurViewSet(viewsets.ModelViewSet):
    queryset = Joueur.objects.all()
    serializer_class = JoueurSerializer
    def get_queryset(self):
         return Joueur.objects.filter(equipe_id=self.kwargs['equipe_id'])
 


