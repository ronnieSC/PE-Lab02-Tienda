from django.db import models

# Create your models here.
class Salida_Cabecera(models.Model):
    SalCabFec   = models.DateField(verbose_name='Fecha')

    class Meta:
        verbose_name_plural = 'Salidas de productos'

    def __str__(self):
        return '#' + str(self.id)
