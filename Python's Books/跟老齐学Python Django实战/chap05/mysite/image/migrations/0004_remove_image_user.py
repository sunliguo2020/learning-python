# Generated by Django 4.2.5 on 2023-11-29 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0003_image_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='user',
        ),
    ]
