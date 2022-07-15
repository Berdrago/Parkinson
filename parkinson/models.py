
from django.db import models

# Modelo de Datos de Web Parkinson
class Crear_usuario(models.Model):
    name = models.CharField(max_length=20)
    id_u=models.AutoField(primary_key=True)
    nombre_u=models.CharField(max_length=20,verbose_name="Nombre de Usuario")
    edad_u=models.IntegerField(verbose_name="Edad de Usuario")
    correo_u=models.EmailField(max_length=20,verbose_name="Correo de Usuario")
    profesion_u=models.CharField(max_length=20,verbose_name="Profesion de Usuario")
    sex=(
        ('M', 'Masculino',),
        ('F','Femenino',),
    )
    sexo_u=models.CharField(max_length=1,choices=sex,verbose_name="Genero de Usuario")
    fnaci=models.DateField(verbose_name="Fecha de Nacimiento de  Usuario")
    def __str__(self):
        return self.nombre_u
class Validacion_de_usuario(models.Model):
    correo_u_c=models.EmailField(max_length=20,verbose_name="Correo validado de Usuario")
    def __str__(self):
        return self.correo_u_c
class Recuperacion_contraseña(models.Model):
    rc_email=models.EmailField(max_length=20,verbose_name="Contraseña Recuperada de Usuario")
    def __str__(self):
        return self.rc_email
class FORMULARIO(models.Model):
    id_fp=models.AutoField(primary_key=True)
    f_c_f=models.DateField(verbose_name="Fecha de Creacion de Formulario")
    score_t_f=models.IntegerField(verbose_name="Total de Score")
    t_i_m=models.IntegerField(verbose_name="Total de Interaciones en Modulos")
    def __str__(self):
        return self.id_fp
class Creacion_modulo_MBM(models.Model):
    id_mbm=models.AutoField(primary_key=True)
    t_modulo=models.CharField(max_length=240,verbose_name="Titulo del Modulo")
    s_modulo=models.CharField(max_length=240,verbose_name="Subtitulo del Modulo")
    nombre_check=models.CharField(max_length=240, verbose_name="Nombre de Modulo 0", default="")
    nombre_check1=models.CharField(max_length=240,verbose_name="Nombre de Modulo 1", default="")
    nombre_check2=models.CharField(max_length=240,verbose_name="Nombre de Modulo 2", default="")
    nombre_check3=models.CharField(max_length=240,verbose_name="Nombre de Modulo 3", default="")
    nombre_check4=models.CharField(max_length=240,verbose_name="Nombre de Modulo 4", default="")
    n_check=models.IntegerField(verbose_name="Numero de Checkbox")
    score_m=models.IntegerField(verbose_name="Score de Modulo")
    i_m=models.IntegerField(verbose_name="Interaccion de Modulo")
    def __str__(self):
        return self.t_modulo
class Creacion_modulo_ADL(models.Model):
    id_adl=models.AutoField(primary_key=True)
    t_modulo=models.CharField(max_length=20,verbose_name="Titulo del Modulo")
    s_modulo=models.CharField(max_length=20,verbose_name="Subtitulo del Modulo")
    n_check=models.IntegerField(verbose_name="Numero de Checkbox")
    score_m=models.IntegerField(verbose_name="Score de Modulo")
    i_m=models.IntegerField(verbose_name="Interaccion de Modulo")
    def __str__(self):
        return self.t_modulo
class Creacion_modulo_ME(models.Model):
    id_me=models.AutoField(primary_key=True)
    t_modulo=models.CharField(max_length=20,verbose_name="Titulo del Modulo")
    s_modulo=models.CharField(max_length=20,verbose_name="Subtitulo del Modulo")
    n_check=models.IntegerField(verbose_name="Numero de Checkbox")
    score_m=models.IntegerField(verbose_name="Score de Modulo")
    i_m=models.IntegerField(verbose_name="Interaccion de Modulo")
    def __str__(self):
        return self.t_modulo
class Creacion_modulo_CT(models.Model ):
    id_ct=models.AutoField(primary_key=True)
    t_modulo=models.CharField(max_length=20,verbose_name="Titulo del Modulo")
    s_modulo=models.CharField(max_length=20,verbose_name="Subtitulo del Modulo")
    n_check=models.IntegerField(verbose_name="Numero de Checkbox")
    score_m=models.IntegerField(verbose_name="Score de Modulo")
    i_m=models.IntegerField(verbose_name="Interaccion de Modulo")
    def __str__(self):
        return self.t_modulo
class Creacion_modulo_MHYS(models.Model):
    id_mhys=models.AutoField(primary_key=True)
    t_modulo=models.CharField(max_length=20,verbose_name="Titulo del Modulo")
    s_modulo=models.CharField(max_length=20,verbose_name="Subtitulo del Modulo")
    n_check=models.IntegerField(verbose_name="Numero de Checkbox")
    score_m=models.IntegerField(verbose_name="Score de Modulo")
    i_m=models.IntegerField(verbose_name="Interaccion de Modulo")
    def __str__(self):
        return self.t_modulo
class Creacion_modulo_SEADLS(models.Model):
    id_seadls=models.AutoField(primary_key=True)
    t_modulo=models.CharField(max_length=20,verbose_name="Titulo del Modulo")
    s_modulo=models.CharField(max_length=20,verbose_name="Subtitulo del Modulo")
    n_check=models.IntegerField(verbose_name="Numero de Checkbox")
    score_m=models.IntegerField(verbose_name="Score de Modulo")
    i_m=models.IntegerField(verbose_name="Interaccion de Modulo")
    def __str__(self):
        return self.t_modulo

class FORMULARIO_FINALIZADO(models.Model):
    id_ff=models.AutoField(primary_key=True)
    score_ff=models.IntegerField(verbose_name="Score de Formulario Finalizado")
    fc_ff=models.DateField(verbose_name="Fecha de Creacciond de Formulario Finlizado")
    def __str__(self):
        return self.id_ff
class PDF(models.Model):
    id_pdf=models.AutoField(primary_key=True)
    def __str__(self):
        return self.id_pdf
class GRAFICOS_FF(models.Model):
    id_g=models.AutoField(primary_key=True)
    g_ff=models.IntegerField(verbose_name="Total de Formularios Finalizados")
    g_v_d=models.IntegerField(verbose_name="Total Visitas Por dia")
    g_f_d=models.IntegerField(verbose_name="Total Formularios Diarios")
    g_pr=models.IntegerField(verbose_name="Total Personas Registradas Por dia ")
    g_id=models.IntegerField(verbose_name="Total de Interacciones Diarias")
    def __str__(self):
        return self.g_ff

