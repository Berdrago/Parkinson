# Generated by Django 4.0.3 on 2022-07-19 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkinson', '0005_alter_creacion_modulo_mbm_nombre_check_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creacion_modulo_mbm',
            name='t_modulo',
        ),
        migrations.AlterField(
            model_name='creacion_modulo_mbm',
            name='s_modulo',
            field=models.CharField(max_length=240, verbose_name='Subtitulo 1  del Modulo'),
        ),
    ]
