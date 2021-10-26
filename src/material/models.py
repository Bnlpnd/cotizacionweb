from django.db import models
from django.urls import reverse

# Create your models here.
class Material(models.Model):
    codmaterial = models.CharField(max_length=5, null=False)
    nombre = models.CharField(max_length=200, null=False)
    stock = models.IntegerField(default=0)
    costocotizacion = models.DecimalField(decimal_places=2, max_digits=1000, default=0.0)
    
    def get_absolute_url(self):
        return reverse("material:material_detail",kwargs={'id':self.id})
