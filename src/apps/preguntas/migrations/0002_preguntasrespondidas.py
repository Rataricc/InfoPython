# Generated by Django 4.0 on 2022-11-16 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreguntasRespondidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correcta', models.BooleanField(default=False, verbose_name='¿Es esta la respuesta correcta?')),
                ('puntaje_obtenido', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Puntaje Obtenido')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preguntas.pregunta')),
                ('respuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intentos', to='preguntas.elegirrespuesta')),
            ],
        ),
    ]
