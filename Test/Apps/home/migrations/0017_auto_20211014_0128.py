# Generated by Django 3.2.7 on 2021-10-14 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_remove_usuarioadmin_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formularioinscripcion',
            name='antecedentespenales',
            field=models.ImageField(upload_to='Uploaded Files/'),
        ),
        migrations.AlterField(
            model_name='formularioinscripcion',
            name='antecedentespoliciacos',
            field=models.ImageField(upload_to='Uploaded Files/'),
        ),
        migrations.AlterField(
            model_name='formularioinscripcion',
            name='cartaLaboral',
            field=models.ImageField(upload_to='Uploaded Files/'),
        ),
        migrations.AlterField(
            model_name='formularioinscripcion',
            name='cartaRecomendacion',
            field=models.ImageField(upload_to='Uploaded Files/'),
        ),
        migrations.AlterField(
            model_name='formularioinscripcion',
            name='fotografiaDPI',
            field=models.ImageField(upload_to='Uploaded Files/'),
        ),
        migrations.AlterField(
            model_name='formularioinscripcion',
            name='fotografiaPersonal',
            field=models.ImageField(upload_to='Uploaded Files/'),
        ),
        migrations.AlterField(
            model_name='formularioinscripcion',
            name='fotografiaRTU',
            field=models.ImageField(upload_to='Uploaded Files/'),
        ),
        migrations.AlterField(
            model_name='formularioinscripcion',
            name='tituloyDiplomas',
            field=models.ImageField(upload_to='Uploaded Files/'),
        ),
    ]