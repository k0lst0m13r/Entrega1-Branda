# Generated by Django 4.0.5 on 2022-07-14 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0013_alter_post_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(default='', upload_to='blog/'),
        ),
    ]
