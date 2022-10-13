# Generated by Django 3.0.2 on 2022-10-13 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ArtNom', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('ArtDes', models.CharField(blank=True, max_length=100, null=True, verbose_name='Descripción')),
                ('ArtCosUni', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Costo unitario')),
                ('ArtSitAct', models.BooleanField(default=True, verbose_name='Disponible')),
                ('ArtSto', models.IntegerField(default=1, verbose_name='Cantidad en stock')),
                ('ArtCatCod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorias.Categoria', verbose_name='Categoria')),
            ],
        ),
    ]