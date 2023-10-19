from django.urls import path
from .views import IndexView, BlogView, ColetaView,EmpresaColetaView, AgendarColetaView, HistoricoColetaView, DescarteView, LocalDescarteView, AgendarDescarteView, HistoricoDescarteView

urlpatterns = [
    #Modelo de criação de url: path('endereco/',NomedaView.as.view(),name='nome_da_url'),
    path('',IndexView.as_view(), name='index'), #Pagina Inicial
    path('blog/', BlogView.as_view(), name='blog'), #Blog
    path('coleta/', ColetaView.as_view(), name='coleta'),
    path('coleta/empresacoleta', EmpresaColetaView.as_view(), name='empresacoleta'),
    path('coleta/agendarcoleta', AgendarColetaView.as_view(), name='agendarcoleta'),
    path('coleta/historicocoleta',HistoricoColetaView.as_view(), name='historicocoleta'),
    path('descarte/', DescarteView.as_view(), name='descarte'),
    path('descarte/localdescarte',LocalDescarteView.as_view(), name='localdescarte'),
    path('descarte/agendardescarte', AgendarDescarteView.as_view(), name='agendardescarte'),
    path('descarte/historidescarte',HistoricoDescarteView.as_view(), name='historicodescarte'),
]