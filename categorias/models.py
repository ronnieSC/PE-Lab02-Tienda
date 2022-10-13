from django.db import models

# Create your models here.
class Categoria(models.Model):
    CatDes  = models.CharField(verbose_name='Descripción', max_length=50, unique=True)

    def __str__(self):
        return self.CatDes
