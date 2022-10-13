from django.db import models
from categorias.models import Categoria
from ingresos.models import Ingreso_Cabecera
from presentaciones.models import Presentacion
from salidas.models import Salida_Cabecera

# Create your models here.
class Articulo(models.Model):
    ArtNom      = models.CharField(verbose_name='Nombre', max_length=50, unique=True)
    ArtDes      = models.CharField(verbose_name='Descripción', max_length=100, blank=True, null=True)
    ArtCatCod   = models.ForeignKey(Categoria, verbose_name='Categoria', on_delete=models.CASCADE)
    ArtCosUni   = models.DecimalField(verbose_name='Costo unitario', max_digits=5, decimal_places=2)
    ArtSitAct   = models.BooleanField(verbose_name='Disponible', default=True)
    ArtSto      = models.IntegerField(verbose_name='Cantidad en stock', default=1)

    def __str__(self):
        return self.ArtNom

class Ingreso_Detalle(models.Model):
    class Meta:
        verbose_name_plural = 'Detalle de ingresos de productos'
        unique_together = (('IngDetCabCod', 'IngDetArtNom'))

    IngDetCabCod    = models.ForeignKey(Ingreso_Cabecera, verbose_name='Código de documento de ingreso', on_delete=models.CASCADE)
    IngDetArtNom    = models.ForeignKey(Articulo, verbose_name='Artículo ingresado', on_delete=models.CASCADE)
    IngDetPreDes    = models.ForeignKey(Presentacion, verbose_name='Presentación del artículo', on_delete=models.CASCADE)
    IngDetCan       = models.IntegerField(verbose_name='Cantidad')
    IngDetCosUni    = models.DecimalField(verbose_name='Costo unitario', max_digits=10, decimal_places=2)

    def __str__(self):
        return 'Artículo ' + self.IngDetArtNom.ArtNom + ' ingresado'

    @property
    def sumarStock(self):
        suma = self.IngDetCan + self.IngDetArtNom.ArtSto
        print(suma)

        return suma

    def save(self):
        articulo = Articulo.objects.get(ArtNom=self.IngDetArtNom.ArtNom)
        articulo.ArtSto = self.sumarStock
        articulo.save()

        super (Ingreso_Detalle, self).save()

class Salida_Detalle(models.Model):
    class Meta:
        unique_together = (('SalDetCabCod', 'SalDetArtNom'))
        verbose_name_plural = 'Detalle de salida de productos'

    SalDetCabCod    = models.ForeignKey(Salida_Cabecera, verbose_name='Número de factura', on_delete=models.CASCADE)
    SalDetArtNom    = models.ForeignKey(Articulo, verbose_name='Artículo', on_delete=models.CASCADE)
    SalDetPreDes    = models.ForeignKey(Presentacion, verbose_name='Unidad de medida', on_delete=models.CASCADE)
    SalDetCosUni    = models.DecimalField(verbose_name='Costo unitario', max_digits=10, decimal_places=2)
    SalDetCan       = models.IntegerField(verbose_name='Cantidad')

    def __str__(self):
        return str(self.SalDetCabCod) + '-' + str(self.SalDetArtNom)

    @property
    def restarStock(self):
        resta = 0

        if self.SalDetCan < self.SalDetArtNom.ArtSto:
            resta = self.SalDetArtNom.ArtSto - self.SalDetCan

        return resta

    def save(self):
        articulo = Articulo.objects.get(ArtNom=self.SalDetArtNom.ArtNom)
        articulo.ArtSto = self.restarStock
        articulo.save()

        super (Salida_Detalle, self).save()
