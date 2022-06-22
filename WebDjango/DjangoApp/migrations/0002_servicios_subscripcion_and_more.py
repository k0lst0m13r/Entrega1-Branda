# Generated by Django 4.0.5 on 2022-06-22 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Subscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=40)),
            ],
        ),
        migrations.RenameField(
            model_name='comentarios',
            old_name='coment',
            new_name='comentario',
        ),
    ]
