# Generated by Django 2.2.13 on 2020-07-27 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mortem',
            new_name='Posts',
        ),
    ]
