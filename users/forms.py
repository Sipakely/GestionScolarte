from django import forms
from .models import Etudiant

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'email', 'age']

    def clean_nom(self):
        nom = self.cleaned_data.get('nom')
        if len(nom) < 2:
            raise forms.ValidationError("Nom trop court")
        return nom

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if "@" not in email:
            raise forms.ValidationError("Email invalide")
        return email

    def clean(self):
        cleaned_data = super().clean()
        age = cleaned_data.get('age')

        if age is not None and age < 16:
            raise forms.ValidationError("Âge minimum 16 ans")

        return cleaned_data