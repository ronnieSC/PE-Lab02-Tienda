from django.db import models

# Create your models here.
class Proveedor(models.Model):
    ProNom      = models.CharField(verbose_name='Nombre del Proveedor', max_length=200)
    ProDir      = models.CharField(verbose_name='Dirección', max_length=200, null=True, blank=True)
    ProTel      = models.CharField(verbose_name='Teléfono', max_length=15, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.ProNom
