# Generated by Django 3.2 on 2021-05-11 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Datos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dato',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='Datosimg', verbose_name='Imagen'),
        ),
    ]
