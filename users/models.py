from django.db import models
class User(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'Utilisateur'),
    )

    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.nom

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_naissance = models.DateField()
    classe = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nom} {self.prenom}"