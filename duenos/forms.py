from django import forms
from .models import Dueno

class DueñoForm(forms.ModelForm):
    class Meta:
        model = Dueno
        fields = '__all__'
