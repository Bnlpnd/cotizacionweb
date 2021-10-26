from django import forms
from django.forms.fields import NullBooleanField
from .models import Cotizacion

   
class CotizacionForm(forms.ModelForm):
    fechacotizacion = forms.DateTimeField
    instalacion      = forms.BooleanField
    precioinstalacion   = forms.DecimalField(initial=50.0)
    preciocotizacion   = forms.DecimalField(initial=0.0)


#Inicializando 
    class Meta:
        model = Cotizacion
        fields = "__all__"

