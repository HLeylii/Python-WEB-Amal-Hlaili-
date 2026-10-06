from django.db import models
from EntrepriseApp.models import Entreprise
# Create your models here.
class Expedition(models.Model):
    refenrence=models.CharField(max_length=20, 
                                unique=True,
                                editable=False,
                                )
    date_souhaitee=models.DateField()
    ville_depart=models.CharField(max_length=100)
    ville_arrivee=models.CharField(max_length=100)

    poids_kg=models.DecimalField(max_digits=10, decimal_places=2)

    stattus=models.CharField(max_length=20,
                             choices=[
                                 ('pbliee','Publiée'),
                                 ('attribuee','Attribuée'),
                                 ('en_cours','En cours'),
                                 ('livree','Livrée'),
                                 ('annulee','Annulée'),  
                             ], default='publiee'
                             )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    entreprise=models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='expeditions')

