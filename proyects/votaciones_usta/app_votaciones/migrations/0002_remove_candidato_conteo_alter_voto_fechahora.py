# Generated by Django 4.0.4 on 2022-05-17 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_votaciones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidato',
            name='conteo',
        ),
        migrations.AlterField(
            model_name='voto',
            name='fechaHora',
            field=models.DateTimeField(),
        ),
    ]
