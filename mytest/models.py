from django.db import models
from django.urls import reverse

# Create your models here.


class Equipe(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=30)
    drapeau = models.CharField(max_length=30)
    def __str__(self):
        return self.nom


    def get_absolute_url(self):
        return reverse('equip:equipe_edit', kwargs={'id': self.id})


class Joueur(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=30)
    num = models.IntegerField()
    present = models.BooleanField(default=True)
    equipe_id = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
