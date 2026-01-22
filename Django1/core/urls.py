from django.urls import path
from .views import index,contato,tecnologias,produto

urlpatterns = [
    path('',index, name="index"),
    path('contato',contato, name="contato"),
    path('tec', tecnologias,name='tecnologia'),
    path('produto/<int:pk>', produto, name='produto')
]