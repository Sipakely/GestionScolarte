from django.db import models

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.nom