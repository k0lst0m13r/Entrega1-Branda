# Generated by Django 4.0.5 on 2022-07-10 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0008_post_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(default='algo', upload_to='media/'),
        ),
    ]
