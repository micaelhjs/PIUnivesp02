from django.urls import path
from .views import IndexView

urlpatterns = {
    #Modelo de criação de url: path('endereco/',NomedaView.as.view(),name='nome_da_url'),
    path('',IndexView.as_view(), name='inicio'), #Pagina Inicial
}