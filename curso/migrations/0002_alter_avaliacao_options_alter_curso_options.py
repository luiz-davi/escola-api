# Generated by Django 4.0 on 2023-06-07 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='avaliacao',
            options={'ordering': ['criacao'], 'verbose_name': 'Avaliação', 'verbose_name_plural': 'Avaliações'},
        ),
        migrations.AlterModelOptions(
            name='curso',
            options={'ordering': ['criacao'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
    ]
