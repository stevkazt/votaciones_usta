# Generated by Django 4.0.4 on 2022-05-19 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_votaciones', '0002_alter_votacion_semestre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votacion',
            name='semestre',
            field=models.IntegerField(default=10),
        ),
    ]
