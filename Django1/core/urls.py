from django.urls import path
from .views import index,cliente,tecnologias,produto

urlpatterns = [
    path('',index, name='index'),
    path('contato/<int:pk>',cliente, name='cliente'),
    path('tec/<int:pk>', tecnologias,name='tecnologia'),
    path('produto/<int:pk>', produto, name='produto')
]