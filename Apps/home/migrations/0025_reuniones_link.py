# Generated by Django 3.2.7 on 2021-10-28 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_merge_20211028_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='reuniones',
            name='link',
            field=models.CharField(default=0.000172105931200654, max_length=150),
            preserve_default=False,
        ),
    ]
