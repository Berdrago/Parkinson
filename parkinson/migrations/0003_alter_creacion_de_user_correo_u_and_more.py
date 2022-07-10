# Generated by Django 4.0.3 on 2022-07-10 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkinson', '0002_rename_c_user_creacion_de_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creacion_de_user',
            name='correo_u',
            field=models.EmailField(max_length=20, verbose_name='Correo de Usuario'),
        ),
        migrations.AlterField(
            model_name='creacion_de_user',
            name='edad_u',
            field=models.IntegerField(verbose_name='Edad de Usuario'),
        ),
        migrations.AlterField(
            model_name='creacion_de_user',
            name='fnaci',
            field=models.DateField(verbose_name='Fecha de Nacimiento de  Usuario'),
        ),
        migrations.AlterField(
            model_name='creacion_de_user',
            name='nombre_u',
            field=models.CharField(max_length=20, verbose_name='Nombre de Usuario'),
        ),
        migrations.AlterField(
            model_name='creacion_de_user',
            name='profesion_u',
            field=models.CharField(max_length=20, verbose_name='Profesion de Usuario'),
        ),
        migrations.AlterField(
            model_name='creacion_de_user',
            name='sexo_u',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, verbose_name='Genero de Usuario'),
        ),
        migrations.AlterField(
            model_name='creacion_modulo_adl',
            name='i_m',
            field=models.IntegerField(verbose_name='Interaccion de Modulo'),
        ),
        migrations.AlterField(
            model_name='creacion_modulo_adl',
            name='n_check',
            field=models.IntegerField(verbose_name='Numero de Checkbox'),
        ),
        migrations.AlterField(
            model_name='creacion_modulo_adl',
            name='s_modulo',
            field=models.CharField(max_length=20, verbose_name='Subtitulo del Modulo'),
        ),
        migrations.AlterField(
            model_name='creacion_modulo_adl',
            name='score_m',
            field=models.IntegerField(verbose_name='Score de Modulo'),
        ),
        migrations.AlterField(
            model_name='creacion_modulo_adl',
            name='t_modulo',
            field=models.CharField(max_length=20, verbose_name='Titulo del Modulo'),
        ),
        migrations.AlterField(
            model_name='creacion_modulo_mbm',
            name='i_m',
            field=models.IntegerField(verbose_name='Interaccion de Modulo'),
        ),
        migrations.AlterField(
            model_name='creacion_modulo_mbm',
            name='n_check',
            field=models.IntegerField(verbose_name='Numero de Checkbox'),
        ),
        migrations.AlterField(
            model_name='creacion_modulo_mbm',
            name='s_modulo',
            field=models.CharField(max_length=20, verbose_name='Subtitulo del Modulo'),
        ),
        migrations.AlterField(
            model_name='creacion_modulo_mbm',
            name='score_m',
            field=models.IntegerField(verbose_name='Score de Modulo'),
        ),
        migrations.AlterField(
            model_name='creacion_modulo_mbm',
            name='t_modulo',
            field=models.CharField(max_length=20, verbose_name='Titulo del Modulo'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='f_c_f',
            field=models.DateField(verbose_name='Fecha de Creacion de Formulario'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='score_t_f',
            field=models.IntegerField(verbose_name='Total de Score'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='t_i_m',
            field=models.IntegerField(verbose_name='Total de Interaciones en Modulos'),
        ),
        migrations.AlterField(
            model_name='formulario_finalizado',
            name='fc_ff',
            field=models.DateField(verbose_name='Fecha de Creacciond de Formulario Finlizado'),
        ),
        migrations.AlterField(
            model_name='formulario_finalizado',
            name='score_ff',
            field=models.IntegerField(verbose_name='Score de Formulario Finalizado'),
        ),
        migrations.AlterField(
            model_name='graficos_ff',
            name='g_f_d',
            field=models.IntegerField(verbose_name='Total Formularios Diarios'),
        ),
        migrations.AlterField(
            model_name='graficos_ff',
            name='g_ff',
            field=models.IntegerField(verbose_name='Total de Formularios Finalizados'),
        ),
        migrations.AlterField(
            model_name='graficos_ff',
            name='g_id',
            field=models.IntegerField(verbose_name='Total de Interacciones Diarias'),
        ),
        migrations.AlterField(
            model_name='graficos_ff',
            name='g_pr',
            field=models.IntegerField(verbose_name='Total Personas Registradas Por dia '),
        ),
        migrations.AlterField(
            model_name='graficos_ff',
            name='g_v_d',
            field=models.IntegerField(verbose_name='Total Visitas Por dia'),
        ),
        migrations.AlterField(
            model_name='recuperacion_contraseña_user',
            name='rc_email',
            field=models.EmailField(max_length=20, verbose_name='Contraseña Recuperada de Usuario'),
        ),
        migrations.AlterField(
            model_name='validacion_correo_usuarios',
            name='correo_u_c',
            field=models.EmailField(max_length=20, verbose_name='Correo validado de Usuario'),
        ),
    ]
