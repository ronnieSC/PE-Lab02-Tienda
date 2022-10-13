from django.db import models

from proveedores.models import Proveedor

# Create your models here.
class Ingreso_Cabecera(models.Model):
    IngCabCod       = models.CharField(verbose_name='Código del documento de ingreso', max_length=50, unique=True)
    IngCabFec       = models.DateField(verbose_name='Fecha de ingreso')
    IngCabProCod    = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Ingresos'

    def __str__(self):
        return '#' + self.IngCabCod
