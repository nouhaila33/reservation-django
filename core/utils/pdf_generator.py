from io import BytesIO
from django.http import FileResponse
from reportlab.pdfgen import canvas
from core.models import Reservation

def generer_pdf_reservations():
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    y = 800
    reservations = Reservation.objects.all()
    p.drawString(100, y, "Liste des Réservations")
    y -= 40
    for r in reservations:
        ligne = f"{r.date} | {r.salle.nom} | {r.heure_debut}-{r.heure_fin} | {r.utilisateur.username}"
        p.drawString(100, y, ligne)
        y -= 20
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='reservations.pdf')


def generer_pdf_reservations():
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    y = 800
    reservations = Reservation.objects.all()
    p.drawString(100, y, "Liste des Réservations")
    y -= 40
    for r in reservations:
        ligne = f"{r.date} | {r.salle.nom} | {r.heure_debut}-{r.heure_fin} | {r.utilisateur.username}"
        p.drawString(100, y, ligne)
        y -= 20
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='reservations.pdf')


def generer_pdf_reservations():
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    y = 800
    reservations = Reservation.objects.all()
    p.drawString(100, y, "Liste des Réservations")
    y -= 40
    for r in reservations:
        ligne = f"{r.date} | {r.salle.nom} | {r.heure_debut}-{r.heure_fin} | {r.utilisateur.username}"
        p.drawString(100, y, ligne)
        y -= 20
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='reservations.pdf')


def generer_pdf_reservations():
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    y = 800
    reservations = Reservation.objects.all()
    p.drawString(100, y, "Liste des Réservations")
    y -= 40
    for r in reservations:
        ligne = f"{r.date} | {r.salle.nom} | {r.heure_debut}-{r.heure_fin} | {r.utilisateur.username}"
        p.drawString(100, y, ligne)
        y -= 20
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='reservations.pdf')