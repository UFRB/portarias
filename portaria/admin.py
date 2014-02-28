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

from django.contrib import admin

import datetime

from .models import Servidor, Portaria


class ServidorAdmin(admin.ModelAdmin):

    search_fields = ['matricula', 'nome']
    list_display = ('matricula', 'nome')


class PortariaAdmin(admin.ModelAdmin):

    fields = ['tipo', 'interessados', 'data', 'arquivo', 'ativa']
    search_fields = ['codigo']
    list_display = ('__unicode__', 'tipo', 'data', 'responsavel', 'ativa')
    list_filter = ('data', 'responsavel', 'ativa', 'tipo')
    filter_horizontal = ('interessados',)


    def save_model(self, request, obj, form, change):
        if obj.codigo is None:
            quantidade = Portaria.objects.filter(
                            data__year=datetime.date.today().year
                            ).count()
            if quantidade:
                obj.codigo = quantidade + 1
            else:
                obj.codigo = 1

            obj.responsavel = request.user
            obj.save()
        else:
            obj.save()

admin.site.register(Servidor, ServidorAdmin)
admin.site.register(Portaria, PortariaAdmin)