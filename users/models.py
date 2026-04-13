from django.db import models

class Etudiant(models.Model):
    school_name = models.CharField(max_length=255, blank=True, default='')
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField(default=18)
    def __str__(self):
        return self.nom

class School(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class UserAccount(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username
