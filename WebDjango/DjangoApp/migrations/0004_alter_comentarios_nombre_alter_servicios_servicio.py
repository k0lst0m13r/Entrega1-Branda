# Generated by Django 4.0.5 on 2022-06-22 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0003_comentarios_creado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='nombre',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='servicios',
            name='servicio',
            field=models.CharField(max_length=30),
        ),
    ]
