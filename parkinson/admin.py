from django.contrib import admin

# Registrar Tablas en panel de Administrador 
from parkinson.models import Crear_usuario
from parkinson.models import Validacion_de_usuario
from parkinson.models import Recuperacion_contraseña
from parkinson.models import Creacion_modulo_ME
from parkinson.models import Creacion_modulo_MHYS
from parkinson.models import Creacion_modulo_SEADLS
from parkinson.models import Creacion_modulo_CT
from parkinson.models import Creacion_modulo_ADL
from parkinson.models import CREACION_MODULO_MBM
from parkinson.models import FORMULARIO_FINALIZADO
from parkinson.models import FORMULARIO
from parkinson.models import GRAFICOS_FF
from parkinson.models import PDF 

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
    list_display=("s_modulo",)
    search_fields=("s_modulo",)
    list_filter=("s_modulo",)
    def get_queryset(self, request):
        ordering = CREACION_MODULO_MBM.objects.all().order_by('id_mbm')
        return ordering
    
class MODULO2(admin.ModelAdmin):
    list_display=("t_modulo",)
    search_fields=("t_modulo",)
    list_filter=("s_modulo",)
class MODULO3(admin.ModelAdmin):
    list_display=("t_modulo",)
    search_fields=("t_modulo",)
    list_filter=("s_modulo",)
class MODULO4(admin.ModelAdmin):
    list_display=("t_modulo",)
    search_fields=("t_modulo",)
    list_filter=("s_modulo",)
class MODULO5(admin.ModelAdmin):
    list_display=("t_modulo",)
    search_fields=("t_modulo",)
    list_filter=("s_modulo",)
class MODULO6(admin.ModelAdmin):
    list_display=("t_modulo",)
    search_fields=("t_modulo",)
    list_filter=("s_modulo",)
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
admin.site.register(Crear_usuario ,ADMIN)
admin.site.register(Validacion_de_usuario,VALIDACION)
admin.site.register(FORMULARIO,FORM)
admin.site.register(Recuperacion_contraseña ,RECUPERACION)
admin.site.register(CREACION_MODULO_MBM ,MODULO1)
admin.site.register(Creacion_modulo_ADL,MODULO2)
admin.site.register(Creacion_modulo_ME,MODULO3)
admin.site.register(Creacion_modulo_CT,MODULO4)
admin.site.register(Creacion_modulo_MHYS,MODULO5)
admin.site.register(Creacion_modulo_SEADLS,MODULO6)
admin.site.register(FORMULARIO_FINALIZADO,FORMF)
admin.site.register(PDF,PFF_F)
admin.site.register(GRAFICOS_FF,GRAF_F)
