from rest_framework import serializers
from .models import Equipe, Joueur



class EquipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipe
        fields = ('id', 'nom', 'drapeau')



class JoueurSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Joueur
        fields = ('id', 'nom', 'num', 'present', 'equipe_id')        





