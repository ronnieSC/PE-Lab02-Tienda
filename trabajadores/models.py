from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trabajador(models.Model):
    TraNomUsu       = models.OneToOneField(User, verbose_name='Nombre de usuario', unique=True, on_delete=models.CASCADE)

    Masculino = 'M'
    Femenino = 'F'
    sexo_del_trabajador = [
        (Masculino, 'Masculino'),
        (Femenino, 'Femenino'),
    ]

    TraSex      = models.CharField(verbose_name='Sexo del trabajador', max_length=1, choices=sexo_del_trabajador, default=Masculino, null=True, blank=True)
    TraFecNac   = models.DateField(verbose_name='Fecha de nacimiento', null=True, blank=True)
    TraDNI      = models.CharField(verbose_name='DNI', max_length=15, null=True, blank=True)

    class Meta:
        verbose_name_plural='Trabajadores'

    def __str__(self):
        return self.TraNomUsu.first_name + ' ' + self.TraNomUsu.last_name
