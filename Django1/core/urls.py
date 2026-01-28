from django.urls import path
from .views import index,cliente,tecnologias,produto,estudo

urlpatterns = [
    path('',index, name='index'),
    path('contato/<int:pk>',cliente, name='cliente'),
    path('tec/<int:pk>', tecnologias,name='tecnologia'),
    path('produto/<int:pk>', produto, name='produto'),
    path('estudos/<int:pk>', estudo, name='estudo')
]