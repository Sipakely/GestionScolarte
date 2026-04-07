from django import forms
from .models import Matiere

class MatiereForm(forms.ModelForm):
    class Meta:
        model = Matiere
        fields = ['nom', 'coefficient']

    def clean_nom(self):
        nom = self.cleaned_data.get('nom')
        if len(nom) < 2:
            raise forms.ValidationError("Nom trop court")
        return nom

    def clean_coefficient(self):
        coef = self.cleaned_data.get('coefficient')

        if coef <= 0:
            raise forms.ValidationError("Le coefficient doit être supérieur à 0")

        return coef 