from django.db import models
from django.urls import reverse

# Create your models here.
class Venta(models.Model):
    codventa = models.CharField(default='00000',max_length=5)
    fechaventa = models.DateTimeField(auto_now_add=True)
    preciototal = models.DecimalField(decimal_places=2, max_digits=1000, default=0.0)
    montocancelado = models.DecimalField(decimal_places=2, max_digits=1000, default=0.0)
    saldo = models.DecimalField(decimal_places=2, max_digits=1000, default=0.0)
    estado = models.CharField(default='PEN', max_length=3) #1.PEN pendiente, 2.CAN cancelado, 3.ANU anulado
    
    def get_absolute_url(self):
        return reverse("venta:venta_detail",kwargs={'id':self.id})
