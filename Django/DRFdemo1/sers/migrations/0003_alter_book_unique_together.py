# Generated by Django 3.2 on 2023-07-19 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sers', '0002_rename_titile_book_title'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('title', 'put_date')},
        ),
    ]
