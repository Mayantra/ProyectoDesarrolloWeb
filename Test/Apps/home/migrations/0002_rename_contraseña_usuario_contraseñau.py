# Generated by Django 3.2.6 on 2021-10-19 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='contraseña',
            new_name='contraseñau',
        ),
    ]
