# Generated by Django 3.2 on 2021-05-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Datos', '0005_remove_dato_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dato',
            name='autor',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Autor'),
        ),
    ]
