from django.urls import path, include
from django.conf.urls import url, include
from .models import Equipe, Joueur
from . import views 
from rest_framework import routers
from django.template.response import TemplateResponse

router = routers.DefaultRouter()
router.register('equipes', views.EquipeViewSet)
router.register('joueurs', views.JoueurViewSet)

urlpatterns = [

    path('', include(router.urls)),
    path('<int:equipe_id>/joueurs/', include(router.urls)),
	path('equipe', views.equipe_list, name='equipe_list'),
    path('view-equipe/<int:id>', views.equipe_view, name='equipe_view'),
    path('new-equipe', views.equipe_create, name='equipe_new'),
    path('edit-equipe/<int:id>', views.equipe_update, name='equipe_edit'),
    path('joueur', views.joueur_list, name='joueur_list'),
    path('view-joueur/<int:id>', views.joueur_view, name='joueur_view'),
    path('new-joueur', views.joueur_create, name='joueur_new'),
    path('edit-joueur/<int:id>', views.joueur_update, name='joueur_edit'),

]