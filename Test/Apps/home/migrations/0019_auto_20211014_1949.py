# Generated by Django 3.2.7 on 2021-10-15 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20211014_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asistencia',
            name='IDFormulario',
        ),
        migrations.AddField(
            model_name='asistencia',
            name='IDUsuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.usuario'),
        ),
    ]
