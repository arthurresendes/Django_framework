from django.urls import path
from .views import index,contato,tecnologias

urlpatterns = [
    path('',index),
    path('contato',contato),
    path('tec', tecnologias)
]