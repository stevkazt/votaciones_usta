# Generated by Django 4.0.4 on 2022-05-05 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_votaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semestre', models.IntegerField()),
                ('propuesta', models.CharField(max_length=200)),
                ('idEstudiante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='candidatos', to='app_votaciones.estudiante')),
                ('idVotacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='candidatos', to='app_votaciones.votacion')),
            ],
        ),
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaHora', models.DateField()),
                ('idCandidato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='votos', to='app_votaciones.candidato')),
                ('idVotante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='votos', to='app_votaciones.estudiante')),
            ],
        ),
    ]