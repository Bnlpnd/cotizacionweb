from django import forms
from .models import Modelo

class ModeloForm(forms.ModelForm):
    nombre      = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Nombre"}))
    descripcion = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Descripción"}))
    diaselaboracion   = forms.IntegerField(initial=8)

#Inicializando 
    class Meta:
        model = Modelo
        fields = "__all__"
