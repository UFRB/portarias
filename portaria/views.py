# -*- coding: utf-8 -*-
#
#  Copyright (c) 2014 Wille Marcel Lima Malheiro and contributors
#
#  This file is part of Portaria.
#
#  Portaria is free software under terms of the GNU Affero General Public
#  License version 3 (AGPLv3) as published by the Free
#  Software Foundation. See the file README for copying conditions.
#
import unicodecsv

from django.views.generic import ListView
from django.db.models import Q
from django.http import HttpResponse

from .models import Portaria


class Index(ListView):
    queryset = Portaria.objects.all().filter(ativa=True).order_by('-codigo')
    context_object_name = 'portarias'
    paginate_by = 20


class Relatorio(ListView):
    """View que lista as portarias com os nomes dos funcionários responsáveis e
    sem a coluna de Download. Foi planejada apenas para uso interno e para
    impressão."""

    queryset = Portaria.objects.all().order_by('codigo')
    context_object_name = 'portarias'
    template_name = "portaria/relatorio.html"


class Search(ListView):
    template_name = "portaria/portaria_list.html"

    def get_queryset(self):
        self.query = self.request.GET.get('search', '')

    def get_context_data(self, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)

        if self.query:
            qset = (
                Q(interessados__nome__icontains=self.query) |
                Q(interessados__matricula__icontains=self.query) |
                Q(tipo__icontains=self.query) |
                Q(codigo__icontains=self.query)
            )
            context['portarias'] = Portaria.objects.filter(ativa=True) \
                .filter(qset).order_by('-codigo').distinct()
        else:
            context['portarias'] = []

        context['query'] = self.query
        return context


def ExportarPortarias(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="portarias.csv"'

    writer = unicodecsv.writer(response, encoding='utf-8')
    writer.writerow(['Código', 'Interessados', 'Data', 'Tipo', 'Responsável'])

    for portaria in Portaria.objects.all():
        interessados = ', '.join(
            [interessado.nome for interessado in portaria.interessados.all()]
            )
        writer.writerow([portaria.codigo, interessados,
            portaria.data, portaria.get_tipo_display(), portaria.responsavel])

    return response