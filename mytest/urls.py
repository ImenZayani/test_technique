from django.urls import path, include
from django.conf.urls import url, include
from .models import Equipe, Joueur
from . import views 
from rest_framework import routers

router = routers.DefaultRouter()
router.register('equipes', views.EquipeViewSet)
router.register('joueurs', views.JoueurViewSet)

urlpatterns = [

    path('', include(router.urls)),
    path('<int:equipe_id>/joueurs/', include(router.urls)),

]