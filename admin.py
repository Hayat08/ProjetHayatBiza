from django.contrib import admin
from .models import Patient
from .models import Medecin
from .models import RendezVous
from .models import DossierMedical
from .models import Departement
from .models import TacheDepartement

# Register your models here.
admin.site.register(Patient)
admin.site.register(Medecin)
admin.site.register(RendezVous)
admin.site.register(DossierMedical)
admin.site.register(Departement)
admin.site.register(TacheDepartement)