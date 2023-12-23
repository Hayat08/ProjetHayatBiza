from django.shortcuts import render

# Create your views here.
from .models import Patient, Medecin, RendezVous, DossierMedical, Departement, TacheDepartement


def affiche_toutes_les_tables(request):
    patients = Patient.objects.all()
    medecins = Medecin.objects.all()
    rendezvous = RendezVous.objects.all()
    dossiers = DossierMedical.objects.all()
    departements = Departement.objects.all()
    taches = TacheDepartement.objects.all()

    context = {
        'patients' : patients,
        'medecins' : medecins,
        'rendezvous': rendezvous,
        'dossiers'  : dossiers,
        'departements': departements,
        'taches' : taches,
    }
    return render(request,'list.html', context)
    
