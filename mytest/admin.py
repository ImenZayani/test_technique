from django.contrib import admin

# Register your models here.
from .models import (Equipe, Joueur)

admin.site.register(Equipe)
admin.site.register(Joueur)
