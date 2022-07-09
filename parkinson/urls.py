



from django.urls import path
from parkinson.views import index , elements, generic


urlpatterns = [
    path('', index ,  name='index'),#Nueva ruta web 
    path('elements/', elements ,  name='elements'),#Nueva ruta web 
    path('generic/', generic ,  name='generic'),#Nueva ruta web 
]