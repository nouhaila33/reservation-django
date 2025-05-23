from django.contrib import admin
from .models import Salle, Equipement, Reservation, ProfilUtilisateur

admin.site.register(Salle)
admin.site.register(Equipement)
admin.site.register(Reservation)
admin.site.register(ProfilUtilisateur)