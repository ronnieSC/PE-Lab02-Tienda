from django.db import models

# Create your models here.
class Presentacion(models.Model):
    PreDes      = models.CharField(verbose_name='Descripción', max_length=50)

    class Meta:
        verbose_name_plural = 'Presentaciones'

    def __str__(self):
        return self.PreDes
