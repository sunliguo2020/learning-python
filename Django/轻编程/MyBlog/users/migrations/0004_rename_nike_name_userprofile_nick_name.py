# Generated by Django 4.2.5 on 2023-11-07 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_desc_userprofile_gexing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='nike_name',
            new_name='nick_name',
        ),
    ]
