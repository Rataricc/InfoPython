# Generated by Django 4.0 on 2022-11-18 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0003_alter_preguntasrespondidas_table_quizusuario_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preguntasrespondidas',
            old_name='usuario',
            new_name='quizUser',
        ),
    ]