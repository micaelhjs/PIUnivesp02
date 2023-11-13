from django.views.generic.edit import CreateView, UpdateView, DeleteView # Para criar, editar e deletar objetos
from django.views.generic.list import ListView # para listar objetos

from .models import Regiao, Empresa # importar as classes para Região e empresa


from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from django.urls import reverse_lazy

# Create your views here.

class RegiaoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administração"
    model = Regiao
    fields = ['nome']
    template_name = 'cadastros/regiao.html'
    success_url = reverse_lazy('listar-regiao')

class EmpresaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administração"
    model = Empresa
    fields = ['nome','endereco','bairro','cep','telefone','site','coleta','descarte', 'regiao']
    template_name = 'cadastros/cadastroempresa.html'
    success_url = reverse_lazy('listar-empresa')



    # Update

class RegiaoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administração"
    model = Regiao
    fields = ['nome']
    template_name = 'cadastros/regiao.html'
    success_url = reverse_lazy('listar-regiao')

class EmpresaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administração"
    model = Empresa
    fields = ['nome','endereco','bairro','cep','telefone','site','coleta','descarte', 'regiao']
    template_name = 'cadastros/cadastroempresa.html'
    success_url = reverse_lazy('listar-empresa')

    # Delete

class RegiaoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administração"
    model = Regiao
    template_name = 'cadastros/form-deletar.html'
    success_url = reverse_lazy('listar-regiao')

class EmpresaDelete(GroupRequiredMixin,LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administração"
    model = Empresa
    fields = ['nome','endereco','bairro','cep','telefone','site','coleta','descarte', 'regiao']
    template_name = 'cadastros/form-deletar.html'
    success_url = reverse_lazy('listar-empresa')

    #  List

class RegiaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Regiao
    template_name = 'cadastros/listas/regiao.html'

class EmpresaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Empresa
    template_name = 'cadastros/listas/empresa.html'