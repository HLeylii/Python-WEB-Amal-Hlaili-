from django.db import models
from ExpeditionApp.models import Expedition
from EntrepriseApp.models import Entreprise
from VehiculeApp.models import Vehicule


class Offre(models.Model):
    STATUT_CHOICES = [
        ('proposee', 'Proposée'),
        ('acceptee', 'Acceptée'),
        ('refusee', 'Refusée'),
    ]
    prix = models.CharField(max_length=10) 
    delai_jours = models.IntegerField() 
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='proposee')
    date_proposition = models.DateField(auto_now=True) 
    expedition = models.ForeignKey(Expedition, on_delete=models.CASCADE , related_name='offre')
    transporteur = models.ForeignKey(Entreprise, on_delete=models.CASCADE , related_name='offre')
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, null=True , related_name='offre')
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)