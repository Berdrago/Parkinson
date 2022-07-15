from django.forms import ModelForm

from parkinson.models import Creacion_modulo_MBM


class formAgregar (ModelForm):
    class Meta  :
        model = Creacion_modulo_MBM
        fields = '__all__'