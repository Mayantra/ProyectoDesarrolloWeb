# Generated by Django 3.2.7 on 2021-10-15 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20211014_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formularioinscripcion',
            name='antecedentespenales',
            field=models.FileField(upload_to='Uploaded Files/'),
        ),
        migrations.AlterField(
            model_name='formularioinscripcion',
            name='antecedentespoliciacos',
            field=models.FileField(upload_to='Uploaded Files/'),
        ),
        migrations.AlterField(
            model_name='formularioinscripcion',
            name='cartaLaboral',
            field=models.FileField(upload_to='Uploaded Files/'),
        ),
        migrations.AlterField(
            model_name='formularioinscripcion',
            name='cartaRecomendacion',
            field=models.FileField(upload_to='Uploaded Files/'),
        ),
        migrations.AlterField(
            model_name='formularioinscripcion',
            name='fotografiaDPI',
            field=models.FileField(upload_to='Uploaded Files/'),
        ),
        migrations.AlterField(
            model_name='formularioinscripcion',
            name='fotografiaPersonal',
            field=models.FileField(upload_to='Uploaded Files/'),
        ),
        migrations.AlterField(
            model_name='formularioinscripcion',
            name='fotografiaRTU',
            field=models.FileField(upload_to='Uploaded Files/'),
        ),
        migrations.AlterField(
            model_name='formularioinscripcion',
            name='tituloyDiplomas',
            field=models.FileField(upload_to='Uploaded Files/'),
        ),
    ]