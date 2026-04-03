from django.db import models
from users.models import Etudiant
from matieres.models import Matiere

class Note(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    valeur = models.FloatField()

    def __str__(self):
        return f"{self.etudiant} - {self.matiere} : {self.valeur}"
