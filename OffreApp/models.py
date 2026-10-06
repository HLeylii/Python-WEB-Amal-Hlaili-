from django.db import models

# Create your models here.

class Offre(models.Model):
    date_proposition=models.DateField(auto_now_add=True)
    delai_jours=models.PositiveIntegerField()
    prix=models.DecimalField(max_digits=10, decimal_places=2)
    status=models.CharField(max_length=20,
                            choices=[
                                ('propose','Proposé'),
                                ('retire','Retiré'),
                                ('acceptee','Accepté'),
                                ('refusee','Refusée'),
                            ], default='propose' 
                            )

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    expedition=models.ForeignKey('ExpeditionApp.Expedition', on_delete=models.CASCADE, related_name='offres')

    vehicule=models.ForeignKey('VehiculeApp.Vehicule', on_delete=models.CASCADE, related_name='offres')

    tranporteur=models.ForeignKey('EntrepriseApp.Entreprise', on_delete=models.CASCADE, related_name='offres')
    
