from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True, null=True, blank=True)
    password = models.CharField(max_length=128, blank=True, default='')

    def __str__(self):
        return self.name


class UserAccount(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username
