from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('reserver/', views.reserver_salle, name='reserver_salle'),
    path('reservations/', views.liste_reservations, name='liste_reservations'),
    path('salles/', views.gestion_salles, name='gestion_salles'),
    path('equipements/', views.gestion_equipements, name='gestion_equipements'),
    path('calendrier/', views.calendrier, name='calendrier'),
    path('api/reservations/', views.reservations_api, name='api_reservations'),
    path('export/pdf/', views.export_pdf, name='export_pdf'),
    path('calendrier/', views.calendrier, name='calendrier'),
    path('api/reservations/', views.reservations_api, name='api_reservations'),
    path('export/pdf/', views.export_pdf, name='export_pdf'),
    path('calendrier/', views.calendrier, name='calendrier'),
    path('api/reservations/', views.reservations_api, name='api_reservations'),
    path('export/pdf/', views.export_pdf, name='export_pdf'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/dashboard/stats/', views.dashboard_stats_api, name='dashboard_stats_api'),

]
