from django.urls import path
from .views import affiche_toutes_les_tables

urlpatterns = [
    path('',affiche_toutes_les_tables),
   
]

