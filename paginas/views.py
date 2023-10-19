from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"


class BlogView(TemplateView):
    template_name = "blog.html"

class ColetaView(TemplateView):
    template_name = "coleta.html"

class EmpresaColetaView(TemplateView):
    template_name = "empresacoleta.html"

class AgendarColetaView(TemplateView):
    template_name = "agendarcoleta.html"

class HistoricoColetaView(TemplateView):
    template_name = "historicocoleta.html"

class DescarteView(TemplateView):
    template_name = "descarte.html"

class LocalDescarteView(TemplateView):
    template_name = "localdescarte.html"

class AgendarDescarteView(TemplateView):
    template_name = "agendardescarte.html"

class HistoricoDescarteView(TemplateView):
    template_name = "historicodescarte.html"