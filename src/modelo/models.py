from django.db import models
from django.urls import reverse

# Create your models here.
class Modelo(models.Model):
    nombre      = models.CharField(max_length=200  , null=False)
    descripcion = models.CharField(max_length=500, null=True)
    diaselaboracion = models.IntegerField(default=8)

    def get_absolute_url(self):
        return reverse("modelo:modelo_detail",kwargs={'id':self.id})