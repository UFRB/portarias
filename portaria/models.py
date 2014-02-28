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

from django.db import models
from django.contrib.auth.models import User

from filer.fields.file import FilerFileField

# Create your models here.


class Servidor(models.Model):

    matricula = models.IntegerField(unique=True)
    nome = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s - %s' % (self.matricula, self.nome)

    class Meta:
        verbose_name = u'Servidor'
        verbose_name_plural = u'Servidores'


class Portaria(models.Model):

    TIPOS = (
        ('permanencia', 'Abono Permanência'),
        ('insalubridade', 'Adicional de Insalubridade'),
        ('capacitacao', 'Capacitação'),
        ('comissao', 'Comissão'),
        ('designacao', 'Designação'),
        ('dispensa', 'Dispensa'),
        ('lotacao', 'Lotação'),
        ('progressao', 'Progressão'),
        ('remocao', 'Remoção'),
        ('retificacao', 'Retificação'),
        ('substituicao', 'Substituição'),
    )
    codigo = models.IntegerField('Código', unique_for_year="data")
    data = models.DateField()
    tipo = models.CharField(choices=TIPOS, max_length=100)
    interessados = models.ManyToManyField(Servidor)
    responsavel = models.ForeignKey(User, verbose_name="Responsável")
    arquivo = FilerFileField(blank=True, null=True)
    ativa = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s/%s' % (self.codigo, self.data.year)
