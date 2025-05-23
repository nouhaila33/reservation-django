from django.shortcuts import render, redirect
from .models import Reservation, Salle, Equipement
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    reservations = Reservation.objects.all()
    return render(request, 'core/dashboard.html', {'reservations': reservations})

@login_required
def reserver_salle(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.utilisateur = request.user
            reservation.save()
            form.save_m2m()
            return redirect('liste_reservations')
    else:
        form = ReservationForm()
    return render(request, 'core/reservation/form.html', {'form': form})

@login_required
def liste_reservations(request):
    reservations = Reservation.objects.all()
    return render(request, 'core/reservation/list.html', {'reservations': reservations})

@login_required
def gestion_salles(request):
    salles = Salle.objects.all()
    return render(request, 'core/salle/list.html', {'salles': salles})

@login_required
def gestion_equipements(request):
    equipements = Equipement.objects.all()
    return render(request, 'core/equipement/list.html', {'equipements': equipements})

from django.http import JsonResponse
from django.core.mail import send_mail
from .utils.pdf_generator import generer_pdf_reservations

@login_required
def export_pdf(request):
    return generer_pdf_reservations()

@login_required
def calendrier(request):
    return render(request, 'core/reservation/calendar.html')

@login_required
def reservations_api(request):
    data = [
        {
            'title': r.salle.nom,
            'start': f"{r.date}T{r.heure_debut}",
            'end': f"{r.date}T{r.heure_fin}"
        }
        for r in Reservation.objects.all()
    ]
    return JsonResponse(data, safe=False)

# Envoi de mails après réservation
@login_required
def reserver_salle(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.utilisateur = request.user
            reservation.save()
            form.save_m2m()
            if reservation.invite_mails:
                emails = [e.strip() for e in reservation.invite_mails.split(',') if e.strip()]
                send_mail(
                    subject='Invitation à une réunion',
                    message=f"Vous êtes invité à une réunion dans la salle {reservation.salle.nom} le {reservation.date} de {reservation.heure_debut} à {reservation.heure_fin}.",
                    from_email='admin@reservation.com',
                    recipient_list=emails,
                    fail_silently=True,
                )
            return redirect('liste_reservations')
    else:
        form = ReservationForm()
    return render(request, 'core/reservation/form.html', {'form': form})


from django.http import JsonResponse
from django.core.mail import send_mail
from core.utils.pdf_generator import generer_pdf_reservations

@login_required
def export_pdf(request):
    return generer_pdf_reservations()

@login_required
def calendrier(request):
    return render(request, 'core/reservation/calendar.html')

@login_required
def reservations_api(request):
    data = [
        {
            'title': r.salle.nom,
            'start': f"{r.date}T{r.heure_debut}",
            'end': f"{r.date}T{r.heure_fin}"
        }
        for r in Reservation.objects.all()
    ]
    return JsonResponse(data, safe=False)

@login_required
def reserver_salle(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.utilisateur = request.user
            reservation.save()
            form.save_m2m()
            if reservation.invite_mails:
                emails = [e.strip() for e in reservation.invite_mails.split(',') if e.strip()]
                send_mail(
                    subject='Invitation à une réunion',
                    message=f"Vous êtes invité à une réunion dans la salle {reservation.salle.nom} le {reservation.date} de {reservation.heure_debut} à {reservation.heure_fin}.",
                    from_email='admin@reservation.com',
                    recipient_list=emails,
                    fail_silently=True,
                )
            return redirect('liste_reservations')
    else:
        form = ReservationForm()
    return render(request, 'core/reservation/form.html', {'form': form})


from django.http import JsonResponse
from django.core.mail import send_mail
from core.utils.pdf_generator import generer_pdf_reservations
from django.contrib import messages

@login_required
def export_pdf(request):
    return generer_pdf_reservations()

@login_required
def calendrier(request):
    return render(request, 'core/reservation/calendar.html')

@login_required
def reservations_api(request):
    data = [
        {
            'title': r.salle.nom,
            'start': f"{r.date}T{r.heure_debut}",
            'end': f"{r.date}T{r.heure_fin}"
        }
        for r in Reservation.objects.all()
    ]
    return JsonResponse(data, safe=False)

@login_required
def reserver_salle(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.utilisateur = request.user
            reservation.save()
            form.save_m2m()
            if reservation.invite_mails:
                emails = [e.strip() for e in reservation.invite_mails.split(',') if e.strip()]
                send_mail(
                    subject='Invitation à une réunion',
                    message=f"Vous êtes invité à une réunion dans la salle {reservation.salle.nom} le {reservation.date} de {reservation.heure_debut} à {reservation.heure_fin}.",
                    from_email='admin@reservation.com',
                    recipient_list=emails,
                    fail_silently=True,
                )
            messages.success(request, "Réservation enregistrée avec succès et notifications envoyées.")
            return redirect('liste_reservations')
    else:
        form = ReservationForm()
    return render(request, 'core/reservation/form.html', {'form': form})


from calendar import month_name

@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')

@login_required
def dashboard_stats_api(request):
    current_year = now().year
    reservations = Reservation.objects.filter(date__year=current_year)
    by_month = reservations.annotate(month=ExtractMonth('date')).values('month').annotate(count=Count('id')).order_by('month')

    labels = [month_name[m['month']] for m in by_month]
    counts = [m['count'] for m in by_month]

    materiel_counts = Reservation.objects.values('materiel__nom').annotate(count=Count('materiel')).order_by('-count')[:5]
    materiel_labels = [m['materiel__nom'] for m in materiel_counts]
    materiel_values = [m['count'] for m in materiel_counts]

    return JsonResponse({
        'labels': labels,
        'reservations': counts,
        'materiel_labels': materiel_labels,
        'materiel_counts': materiel_values
    })
