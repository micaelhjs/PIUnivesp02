from django.urls import path

from .views import RegiaoCreate, EmpresaCreate, AgendamentoColetaCreate, AgendamentoDescarteCreate
from .views import RegiaoUpdate, EmpresaUpdate, AgendamentoColetaUpdate, AgendamentoDescarteUpdate
from .views import RegiaoDelete, EmpresaDelete, AgendamentoColetaDelete, AgendamentoDescarteDelete
from .views import RegiaoList, EmpresaList, AgendamentoColetaList, AgendamentoDescarteList

urlpatterns = [
    #Modelo de criação de url: path('endereco/',NomedaView.as.view(),name='nome_da_url'),
    path ('cadastros/regiao/', RegiaoCreate.as_view(), name='cadastrar-regiao'),
    path ('cadastros/empresa/', EmpresaCreate.as_view(), name='cadastrar-empresa'),
    path ('descarte/agendardescarte/', AgendamentoDescarteCreate.as_view(), name='cadastrar-descarte'),
    path ('coleta/agendarcoleta', AgendamentoColetaCreate.as_view(), name='cadastrar-coleta'),

    path ('editar/regiao/<int:pk>', RegiaoUpdate.as_view(), name='editar-regiao'),
    path ('editar/empresa/<int:pk>', EmpresaUpdate.as_view(), name='editar-empresa'),
    path ('editar/descarte/<int:pk>', AgendamentoDescarteUpdate.as_view(), name='editar-descarte'),
    path ('editar/coleta/<int:pk>', AgendamentoColetaUpdate.as_view(), name='editar-coleta'),

    path ('deletar/regiao/<int:pk>', RegiaoDelete.as_view(), name='deletar-regiao'),
    path ('deletar/empresa/<int:pk>', EmpresaDelete.as_view(), name='deletar-empresa'),
    path ('deletar/descarte/<int:pk>', AgendamentoDescarteDelete.as_view(), name='deletar-descarte'),
    path ('deletar/coleta/<int:pk>', AgendamentoColetaDelete.as_view(), name='deletar-coleta'),

    path ('listar/regiao', RegiaoList.as_view(), name='listar-regiao'),
    path ('listar/empresa', EmpresaList.as_view(), name='listar-empresa'),
    path ('listar/descarte', AgendamentoDescarteList.as_view(), name='listar-descarte'),
    path ('listar/coleta', AgendamentoColetaList.as_view(), name='listar-coleta'),
]