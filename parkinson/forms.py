from django.forms import ModelForm

from parkinson.models import CREACION_MODULO_MBM


class formAgregar (ModelForm):
    class Meta  :
        model = CREACION_MODULO_MBM
        fields = '__all__'
        