from django.db import models

# Create your models here.

class Vehicule(models.Model):
    immatricule=models.CharField(unique=True)
    capacite_kg=models.PositiveIntegerField()
    disponible=models.BooleanField(default=True)

    type_vehicule=models.CharField(max_length=20,
                                   choices=[
                                       ('camionnette','Camionnette'),
                                       ('fourgon','Fourgon'),
                                       ('camion_porteur','Camion Porteur'),
                                       ('semi_remorque','Semi-Remorque'),
                                       
                                   ])

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    entreprise=models.ForeignKey('EntrepriseApp.Entreprise', on_delete=models.CASCADE, related_name='vehicules')

