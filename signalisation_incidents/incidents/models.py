from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length = 100)

class Incident(models.Model):
    photo = models.ImageField()
    longitude = models.PositiveIntegerField()
    latitude = models.PositiveIntegerField()
    description_texte = models.TextField()
    description_vocale = models.FileField()
    etat = models.TextChoices(value= {"en attente", "traite"})
    date_creation = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
