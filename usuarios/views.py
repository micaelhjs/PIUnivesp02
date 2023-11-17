from typing import Any
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import UsuarioInform
from django.urls import reverse_lazy

class UsuarioCreate(CreateView):
    template_name = "usuarios/form.html"
    form_class = UsuarioInform
    success_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Registrar Novo Usuário"
        context['botao'] = "Cadastrar"

        return context