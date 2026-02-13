from django.urls import path
from .views import index,estoque,produto

urlpatterns = [
    path('',index, name='index'),
    path('estoque/<int:pk>',estoque,name='estoque'),
    path('produto/',produto,name='produto')
]