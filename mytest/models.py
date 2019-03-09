from django.db import models

# Create your models here.


class Equipe(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=30)
    drapeau = models.CharField(max_length=30)



class Joueur(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=30)
    num = models.IntegerField()
    present = models.BooleanField(default=True)
    equipe_id = models.ForeignKey(Equipe, on_delete=models.CASCADE)
