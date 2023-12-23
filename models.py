from django.db import models

# Create your models here.
class Patient (models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    date_naissance = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.nom

class Medecin(models.Model):
    SPECIALITES = [
        ('Cardiologie', 'Cardiologue'),
        ('Neurologie', 'Neurologue'),
        ('Urologie', 'Urologue'),
        ('Rhumatologie', 'Rhumatologue'),
        ('ORL', 'ORL'),
    ]

    medecin_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=20, choices=SPECIALITES)
    numero_telephone = models.CharField(max_length=15, default="05256314")
    adresse_email = models.EmailField(default="example@example.com")

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class RendezVous(models.Model):
    rendezvous_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    date_heure = models.DateTimeField()
    statut = models.CharField(max_length=20, choices=[('confirmé', 'Confirmé'), ('annulé', 'Annulé'), ('en_attente', 'En attente')])
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Rendez-vous avec {self.medecin} le {self.date_heure}"

class DossierMedical(models.Model):
    dossier_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    date_creation = models.DateField(auto_now_add=True)
    informations_medicales = models.TextField(blank=True, null=True)
    resultats_examens = models.TextField(blank=True, null=True)
    traitement_en_cours = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Dossier médical de {self.patient} créé le {self.date_creation}"

class Departement(models.Model):
    CARDIOLOGIE = 'Cardiologie'
    NEUROLOGIE = 'Neurologie'
    UROLOGIE = 'Urologie'
    RHUMATOLOGIE = 'Rhumatologie'
    ORL = 'ORL'

    DEPARTEMENT_CHOICES = [
        (CARDIOLOGIE, 'Cardiologie'),
        (NEUROLOGIE, 'Neurologie'),
        (UROLOGIE, 'Urologie'),
        (RHUMATOLOGIE, 'Rhumatologie'),
        (ORL, 'ORL'),
    ]

    departement_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=20, choices=DEPARTEMENT_CHOICES)

    def __str__(self):
        return self.nom
class TacheDepartement(models.Model):
    tache_id = models.AutoField(primary_key=True)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    description = models.TextField()
    statut = models.CharField(max_length=20, choices=[('en_cours', 'En cours'), ('terminee', 'Terminée'), ('en_attente', 'En attente')])

    def __str__(self):
        return f"Tâche {self.description} pour {self.departement} - {self.medecin}"

