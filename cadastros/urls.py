from django.urls import path

from .views import RegiaoCreate, EmpresaCreate
from .views import RegiaoUpdate, EmpresaUpdate
from .views import RegiaoDelete, EmpresaDelete
from .views import RegiaoList, EmpresaList

urlpatterns = [
    #Modelo de criação de url: path('endereco/',NomedaView.as.view(),name='nome_da_url'),
    path ('cadastros/regiao/', RegiaoCreate.as_view(), name='cadastrar-regiao'),
    path ('cadastros/empresa/', EmpresaCreate.as_view(), name='cadastrar-empresa'),

    path ('editar/regiao/<int:pk>', RegiaoUpdate.as_view(), name='editar-regiao'),
    path ('editar/empresa/<int:pk>', EmpresaUpdate.as_view(), name='editar-empresa'),

    path ('deletar/regiao/<int:pk>', RegiaoDelete.as_view(), name='deletar-regiao'),
    path ('deletar/empresa/<int:pk>', EmpresaDelete.as_view(), name='deletar-empresa'),

    path ('listar/regiao', RegiaoList.as_view(), name='listar-regiao'),
    path ('listar/empresa', EmpresaList.as_view(), name='listar-empresa'),
]