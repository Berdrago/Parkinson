



from django.urls import path
from parkinson.views import formulario, index , elements, generic, index2


urlpatterns = [
    path('', index ,  name='index'),#Nueva ruta web 
    path('elements/', elements ,  name='elements'),#Nueva ruta web 
    path('generic/', generic ,  name='generic'),#Nueva ruta web 
    path('formulario/', formulario ,  name='formulario'),
    path('index2/', index2 ,  name='index2'),##Nueva ruta web 
]