from django.urls import path
from produto import views

app_name = 'produto'

urlpatterns = [
    path('', views.index),
    path('lista_produto/', views.lista_produto, name='lista_produto'),
    path('cadastra_produto/', views.cadastra_produto, name='cadastra_produto'),
    path('atualiza_produto/', views.atualiza_produto, name='atualiza_produto')
]