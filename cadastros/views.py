from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.views.generic.edit import CreateView, UpdateView, DeleteView # Para criar, editar e deletar objetos
from django.views.generic.list import ListView # para listar objetos

from .models import Regiao, Empresa, AgendamentoColeta, AgendamentoDescarte # importar as classes para Região e empresa
from .forms import AgendamentoColetaForm, AgendamentoDescarteForm

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from django.urls import reverse_lazy

from django.shortcuts import get_object_or_404

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

class AgendamentoColetaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = AgendamentoColeta
    form_class = AgendamentoColetaForm
    template_name = 'cadastros/agendamento.html'
    success_url = reverse_lazy('listar-coleta')
    

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

class AgendamentoDescarteCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = AgendamentoDescarte
    form_class = AgendamentoDescarteForm
    template_name = 'cadastros/agendamento.html'
    success_url = reverse_lazy('listar-descarte')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url


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

class AgendamentoDescarteUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administração"
    model = AgendamentoDescarte
    form_class = AgendamentoDescarteForm
    template_name = 'cadastros/agendamento.html'
    success_url = reverse_lazy('listar-descarte')

    def get_object(self, queryset = None):
        self.object = get_object_or_404 (AgendamentoDescarte, pk=self.kwargs['pk'], usuario = self.request.user)
        return self.object

class AgendamentoColetaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = AgendamentoColeta
    form_class = AgendamentoColetaForm
    template_name = 'cadastros/agendamento.html'
    success_url = reverse_lazy('listar-coleta')

    def get_object(self, queryset = None):
        self.object = get_object_or_404 (AgendamentoColeta, pk=self.kwargs['pk'], usuario = self.request.user)
        return self.object

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

class AgendamentoDescarteDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = AgendamentoDescarte
    template_name = 'cadastros/form-deletar.html'
    success_url = reverse_lazy('listar-agendamento')

    def get_object(self, queryset = None):
        self.object = get_object_or_404 (AgendamentoDescarte, pk=self.kwargs['pk'], usuario = self.request.user)
        return self.object

class AgendamentoColetaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = AgendamentoColeta
    template_name = 'cadastros/form-deletar.html'
    success_url = reverse_lazy('listar-agendamento')

    def get_object(self, queryset = None):
        self.object = get_object_or_404 (AgendamentoColeta, pk=self.kwargs['pk'], usuario = self.request.user)
        return self.object

    #  List

class RegiaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Regiao
    template_name = 'cadastros/listas/regiao.html'

class EmpresaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Empresa
    template_name = 'cadastros/listas/empresa.html'

class AgendamentoDescarteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = AgendamentoDescarte
    template_name = 'cadastros/listas/descarte.html'

    def get_queryset(self):
        self.object_list = AgendamentoDescarte.objects.filter(usuario =self.request.user)
        return self.object_list

class AgendamentoColetaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = AgendamentoColeta
    template_name = 'cadastros/listas/coleta.html'

    def get_queryset(self):
        self.object_list = AgendamentoDescarte.objects.filter(usuario =self.request.user)
        return self.object_list