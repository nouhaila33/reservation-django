from django import forms
from .models import Reservation, Salle, Equipement

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['salle', 'equipements', 'date', 'heure_debut', 'heure_fin', 'objet', 'invite_mails']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'heure_debut': forms.TimeInput(attrs={'type': 'time'}),
            'heure_fin': forms.TimeInput(attrs={'type': 'time'}),
        }
