# Generated by Django 4.0.3 on 2022-07-10 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkinson', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='C_USER',
            new_name='CREACION_DE_USER',
        ),
        migrations.RenameModel(
            old_name='C_M_ADL',
            new_name='CREACION_MODULO_ADL',
        ),
        migrations.RenameModel(
            old_name='C_M_ME',
            new_name='CREACION_MODULO_CT',
        ),
        migrations.RenameModel(
            old_name='C_M_SEADLS',
            new_name='CREACION_MODULO_MBM',
        ),
        migrations.RenameModel(
            old_name='C_M_CT',
            new_name='CREACION_MODULO_ME',
        ),
        migrations.RenameModel(
            old_name='C_M_MBM',
            new_name='CREACION_MODULO_MHYS',
        ),
        migrations.RenameModel(
            old_name='C_M_MHYS',
            new_name='CREACION_MODULO_SEADLS',
        ),
        migrations.RenameModel(
            old_name='F_FINALIZADO',
            new_name='FORMULARIO_FINALIZADO',
        ),
        migrations.RenameModel(
            old_name='RC_USER',
            new_name='RECUPERACION_CONTRASEÑA_USER',
        ),
        migrations.RenameModel(
            old_name='V_C_U',
            new_name='VALIDACION_CORREO_USUARIOS',
        ),
        migrations.RenameField(
            model_name='creacion_modulo_ct',
            old_name='id_me',
            new_name='id_ct',
        ),
        migrations.RenameField(
            model_name='creacion_modulo_mbm',
            old_name='id_seadls',
            new_name='id_mbm',
        ),
        migrations.RenameField(
            model_name='creacion_modulo_me',
            old_name='id_ct',
            new_name='id_me',
        ),
        migrations.RenameField(
            model_name='creacion_modulo_mhys',
            old_name='id_mbm',
            new_name='id_mhys',
        ),
        migrations.RenameField(
            model_name='creacion_modulo_seadls',
            old_name='id_mhys',
            new_name='id_seadls',
        ),
    ]