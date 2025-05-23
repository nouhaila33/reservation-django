from django.db import models
from django.contrib.auth.models import User

class Salle(models.Model):
    nom = models.CharField(max_length=100)
    capacite = models.PositiveIntegerField()
    localisation = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nom} ({self.capacite} places)"

class Equipement(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom

class Reservation(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    equipements = models.ManyToManyField(Equipement, blank=True)
    date = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    objet = models.CharField(max_length=255)
    invite_mails = models.TextField(blank=True, help_text="Séparer les emails par une virgule")

    def __str__(self):
        return f"{self.salle.nom} le {self.date} de {self.heure_debut} à {self.heure_fin}"

class ProfilUtilisateur(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Administrateur'),
        ('utilisateur', 'Utilisateur')
    )
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='utilisateur')

    def __str__(self):
        return f"{self.utilisateur.username} - {self.get_role_display()}"