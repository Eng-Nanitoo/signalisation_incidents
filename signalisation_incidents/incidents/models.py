from django.db import models
from django.utils.translation import gettext_lazy as _

class Categorie(models.Model):
    nom = models.CharField(max_length = 100)

class Etat(models.TextChoices):
    ATTENTE = 'AT', _('En Attente')
    TRAITE = 'TR', _('Traite')

class Incident(models.Model):
    photo = models.ImageField()
    longitude = models.PositiveIntegerField()
    latitude = models.PositiveIntegerField()
    description_texte = models.TextField()
    description_vocale = models.FileField()
    etat = models.CharField(choices = Etat.choices,default = Etat.ATTENTE)
    date_creation = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
