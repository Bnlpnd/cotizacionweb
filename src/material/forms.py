from django import forms
from .models import Material

   
class MaterialForm(forms.ModelForm):
    codmaterial = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Codigo"}))
    nombre      = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Nombre"}))
    stock       = forms.IntegerField()
    costocotizacion   = forms.DecimalField(initial=0.0)


#Inicializando 
    class Meta:
        model = Material
        fields = "__all__"
