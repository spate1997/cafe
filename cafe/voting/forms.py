from django import forms
from .models import Dessert

class VoteForm(forms.ModelForm):
    class Meta:
        model = Dessert
        fields = ['name']