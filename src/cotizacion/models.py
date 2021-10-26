from django.db import models
from django.urls import reverse

# Create your models here.
class Cotizacion(models.Model):
    fechacotizacion = models.DateTimeField(auto_now_add=True)
    instalacion = models.BooleanField(default=True, blank=True)
    precioinstalacion = models.DecimalField(decimal_places=2, max_digits=1000, default=50.0)
    preciocotizacion = models.DecimalField(decimal_places=2, max_digits=1000, default=0.0)
    
    def get_absolute_url(self):
        return reverse("cotizacion:cotizacion_detail",kwargs={'id':self.id})
