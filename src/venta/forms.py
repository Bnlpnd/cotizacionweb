from django import forms
from .models import Venta 

class VentaForm(forms.ModelForm):
    codventa = forms.CharField(initial='00000')
    fechaventa = forms.DateTimeField
    preciototal   = forms.DecimalField(initial=0.0)
    montocancelado   = forms.DecimalField(initial=0.0)
    saldo   = forms.DecimalField(initial=0.0)
    estado = forms.CharField(initial='PEN', max_length=3)
 
     
#Inicializando 
    class Meta:
        model = Venta
        fields = "__all__"

 