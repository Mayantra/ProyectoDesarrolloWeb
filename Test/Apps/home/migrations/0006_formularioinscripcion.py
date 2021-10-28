# Generated by Django 3.2.7 on 2021-10-01 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210930_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormularioInscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.CharField(max_length=10)),
                ('sexo', models.CharField(max_length=20)),
                ('dMunicipioDireccionDeRecibido', models.CharField(max_length=250)),
                ('fotografiaPersonal', models.FileField(upload_to='Uploaded Files/')),
                ('cartaRecomendacion', models.FileField(upload_to='Uploaded Files/')),
                ('cartaLaboral', models.FileField(upload_to='Uploaded Files/')),
                ('tituloyDiplomas', models.FileField(upload_to='Uploaded Files/')),
                ('CUI', models.CharField(max_length=15)),
                ('fotografiaDPI', models.FileField(upload_to='Uploaded Files/')),
                ('fotografiaRTU', models.FileField(upload_to='Uploaded Files/')),
                ('antecedentespenales', models.FileField(upload_to='Uploaded Files/')),
                ('antecedentespoliciacos', models.FileField(upload_to='Uploaded Files/')),
                ('creacion', models.DateField(auto_now_add=True)),
                ('actualizacion', models.DateField(auto_now_add=True)),
                ('IDDepartamentos', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.departamento')),
                ('IDusuario', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.usuario')),
            ],
        ),
    ]
