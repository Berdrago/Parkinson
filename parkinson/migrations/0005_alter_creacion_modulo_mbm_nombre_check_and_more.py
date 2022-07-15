# Generated by Django 4.0.3 on 2022-07-14 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkinson', '0004_crear_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creacion_modulo_mbm',
            name='nombre_check',
            field=models.CharField(default='', max_length=240, verbose_name='Nombre de Modulo 0'),
        ),
        migrations.AlterField(
            model_name='creacion_modulo_mbm',
            name='nombre_check1',
            field=models.CharField(default='', max_length=240, verbose_name='Nombre de Modulo 1'),
        ),
        migrations.AlterField(
            model_name='creacion_modulo_mbm',
            name='nombre_check2',
            field=models.CharField(default='', max_length=240, verbose_name='Nombre de Modulo 2'),
        ),
        migrations.AlterField(
            model_name='creacion_modulo_mbm',
            name='nombre_check3',
            field=models.CharField(default='', max_length=240, verbose_name='Nombre de Modulo 3'),
        ),
        migrations.AlterField(
            model_name='creacion_modulo_mbm',
            name='nombre_check4',
            field=models.CharField(default='', max_length=240, verbose_name='Nombre de Modulo 4'),
        ),
        migrations.AlterField(
            model_name='creacion_modulo_mbm',
            name='s_modulo',
            field=models.CharField(max_length=240, verbose_name='Subtitulo del Modulo'),
        ),
        migrations.AlterField(
            model_name='creacion_modulo_mbm',
            name='t_modulo',
            field=models.CharField(max_length=240, verbose_name='Titulo del Modulo'),
        ),
    ]
