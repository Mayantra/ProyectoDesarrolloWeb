# Generated by Django 3.2.7 on 2021-10-01 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_asistencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario_Reuniones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IDFormulario', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.formularioinscripcion')),
                ('IDReuniones', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.reuniones')),
            ],
        ),
    ]