from django.db import models

class Matiere(models.Model):
    school_name = models.CharField(max_length=255, blank=True, default='')
    nom = models.CharField(max_length=100)
    coefficient = models.IntegerField(default=1)

    def __str__(self):
        return self.nom
