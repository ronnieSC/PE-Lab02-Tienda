# Generated by Django 3.0.2 on 2022-10-13 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TraSex', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=1, null=True, verbose_name='Sexo del trabajador')),
                ('TraFecNac', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('TraDNI', models.CharField(blank=True, max_length=15, null=True, verbose_name='DNI')),
                ('TraNomUsu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Nombre de usuario')),
            ],
            options={
                'verbose_name_plural': 'Trabajadores',
            },
        ),
    ]
