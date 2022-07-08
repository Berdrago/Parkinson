from django.contrib import admin

# Registrar Tablas en panel de Administrador 
from parkinson.models import C_M_ADL
from parkinson.models import C_M_MBM
from parkinson.models import V_C_U
from parkinson.models import RC_USER
from parkinson.models import C_M_MBM
from parkinson.models import C_M_ME
from parkinson.models import C_M_MHYS
from parkinson.models import C_M_SEADLS
from parkinson.models import C_USER
from parkinson.models import F_FINALIZADO
from parkinson.models import FORMULARIO
from parkinson.models import GRAFICOS_FF
from parkinson.models import PDF
from parkinson.models import  C_M_CT  

#---------------------------------------------------
class ADMIN(admin.ModelAdmin):
    list_display=("nombre_u",)
    search_fields=("correo_u",)
    list_filter=("nombre_u",)
class VALIDACION(admin.ModelAdmin):
    list_display=("correo_u_c",)
    search_fields=("correo_u_c",)
    list_filter=("correo_u_c",)
class RECUPERACION(admin.ModelAdmin):
    list_display=("rc_email",)
    search_fields=("rc_email",)
    list_filter=("rc_email",)
class FORM(admin.ModelAdmin):
    list_display=("id_fp",)
    search_fields=("f_c_f",)
    list_filter=("id_fp",)
class MODULO1(admin.ModelAdmin):
    list_display=("t_modulo",)
    search_fields=("t_modulo",)
    list_filter=("n_check",)
class MODULO2(admin.ModelAdmin):
    list_display=("t_modulo",)
    search_fields=("t_modulo",)
    list_filter=("n_check",)
class MODULO3(admin.ModelAdmin):
    list_display=("t_modulo",)
    search_fields=("t_modulo",)
    list_filter=("n_check",)
class MODULO4(admin.ModelAdmin):
    list_display=("t_modulo",)
    search_fields=("t_modulo",)
    list_filter=("n_check",)
class MODULO5(admin.ModelAdmin):
    list_display=("t_modulo",)
    search_fields=("t_modulo",)
    list_filter=("n_check",)
class MODULO6(admin.ModelAdmin):
    list_display=("t_modulo",)
    search_fields=("t_modulo",)
    list_filter=("n_check",)
class FORMF(admin.ModelAdmin):
    list_display=("id_ff",)
    search_fields=("fc_ff",)
    list_filter=("id_ff",)
class PFF_F(admin.ModelAdmin):
    list_display=("id_pdf",)
    search_fields=("id_pdf",)
    list_filter=("id_pdf",)
class GRAF_F(admin.ModelAdmin):
    list_display=("g_ff",)
    search_fields=("g_ff",)
    list_filter=("g_ff",)

#------------------------------------------------
admin.site.register(C_USER,ADMIN)
admin.site.register(V_C_U,VALIDACION)
admin.site.register(FORMULARIO,FORM)
admin.site.register(C_M_MBM,MODULO1)
admin.site.register(RC_USER,RECUPERACION)
admin.site.register(C_M_ADL,MODULO2)
admin.site.register(C_M_ME,MODULO3)
admin.site.register(C_M_CT,MODULO4)
admin.site.register(C_M_MHYS,MODULO5)
admin.site.register(C_M_SEADLS,MODULO6)
admin.site.register(F_FINALIZADO,FORMF)
admin.site.register(PDF,PFF_F)
admin.site.register(GRAFICOS_FF,GRAF_F)
