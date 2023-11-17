from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import AgendamentoColeta, AgendamentoDescarte

from django.contrib.auth.models import User

class AgendamentoColetaForm(forms.ModelForm):
    required_css_class ='required'


    data =forms.DateTimeField(
        label='Data/Hora',
        widget=forms.DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type':'datetime-local'}
        ),
        input_formats=('%Y-%m-%dT%H:%M'),
    )

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

    class Meta:
        model = AgendamentoColeta
        fields = ['data', 'descricao', 'local' , 'empresa']

    def __init__(self, *args, **kwargs):
        super(AgendamentoColetaForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class']= 'form-control'

class AgendamentoDescarteForm(forms.ModelForm):
    required_css_class ='required'

    data = forms.DateTimeField(
        label='Data/Hora',
        widget=forms.DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type':'datetime-local'}
        ),
        input_formats=('%Y-%m-%dT%H:%M'),
    )

    class Meta:
        model = AgendamentoDescarte
        fields = ['data', 'descricao' , 'empresa']

    def __init__(self, *args, **kwargs):
        super(AgendamentoDescarteForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class']= 'form-control'