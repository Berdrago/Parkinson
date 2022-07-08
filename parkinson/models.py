
from django.db import models

# Modelo de Datos de Web Parkinson
class C_USER(models.Model):
    id_u=models.AutoField(primary_key=True)
    nombre_u=models.CharField(max_length=20)
    edad_u=models.IntegerField()
    correo_u=models.EmailField(max_length=20)
    profesion_u=models.CharField(max_length=20)
    sex=(
        ('M', 'Masculino',),
        ('F','Femenino',),
    )
    sexo_u=models.CharField(max_length=1,choices=sex)
    fnaci=models.DateField()
    def __str__(self):
        return self.nombre_u
class V_C_U(models.Model):
    correo_u_c=models.EmailField(max_length=20)
    def __str__(self):
        return self.correo_u_c
class RC_USER(models.Model):
    rc_email=models.EmailField(max_length=20)
    def __str__(self):
        return self.rc_email
class FORMULARIO(models.Model):
    id_fp=models.AutoField(primary_key=True)
    f_c_f=models.DateField()
    score_t_f=models.IntegerField()
    t_i_m=models.IntegerField()
    def __str__(self):
        return self.id_fp
class C_M_MBM(models.Model):
    id_mbm=models.AutoField(primary_key=True)
    t_modulo=models.CharField(max_length=20)
    s_modulo=models.CharField(max_length=20)
    n_check=models.IntegerField()
    score_m=models.IntegerField()
    i_m=models.IntegerField()
    def __str__(self):
        return self.t_modulo
class C_M_ADL(models.Model):
    id_adl=models.AutoField(primary_key=True)
    t_modulo=models.CharField(max_length=20)
    s_modulo=models.CharField(max_length=20)
    n_check=models.IntegerField()
    score_m=models.IntegerField()
    i_m=models.IntegerField()
    def __str__(self):
        return self.t_modulo
class C_M_ME(models.Model):
    id_me=models.AutoField(primary_key=True)
    t_modulo=models.CharField(max_length=20)
    s_modulo=models.CharField(max_length=20)
    n_check=models.IntegerField()
    score_m=models.IntegerField()
    i_m=models.IntegerField()
    def __str__(self):
        return self.t_modulo
class C_M_CT(models.Model):
    id_ct=models.AutoField(primary_key=True)
    t_modulo=models.CharField(max_length=20)
    s_modulo=models.CharField(max_length=20)
    n_check=models.IntegerField()
    score_m=models.IntegerField()
    i_m=models.IntegerField()
    def __str__(self):
        return self.t_modulo
class C_M_MHYS(models.Model):
    id_mhys=models.AutoField(primary_key=True)
    t_modulo=models.CharField(max_length=20 )
    s_modulo=models.CharField(max_length=20)
    n_check=models.IntegerField()
    score_m=models.IntegerField()
    i_m=models.IntegerField()
    def __str__(self):
        return self.t_modulo
class C_M_SEADLS(models.Model):
    id_seadls=models.AutoField(primary_key=True)
    t_modulo=models.CharField(max_length=20)
    s_modulo=models.CharField(max_length=20)
    n_check=models.IntegerField()
    score_m=models.IntegerField()
    i_m=models.IntegerField()
    def __str__(self):
        return self.t_modulo

class F_FINALIZADO(models.Model):
    id_ff=models.AutoField(primary_key=True)
    score_ff=models.IntegerField()
    fc_ff=models.DateField()
    def __str__(self):
        return self.id_ff
class PDF(models.Model):
    id_pdf=models.AutoField(primary_key=True)
    def __str__(self):
        return self.id_pdf
class GRAFICOS_FF(models.Model):
    id_g=models.AutoField(primary_key=True)
    g_ff=models.IntegerField()
    g_v_d=models.IntegerField()
    g_f_d=models.IntegerField()
    g_pr=models.IntegerField()
    g_id=models.IntegerField()
    
    def __str__(self):
        return self.g_ff

