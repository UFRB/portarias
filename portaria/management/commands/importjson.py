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

import simplejson

from django.core.management.base import BaseCommand

from ...models import Servidor


class Command(BaseCommand):
    args = 'filename'
    help = 'Import a json file'

    def handle(self, *args, **options):
        for filename in args:
            data_json = open(filename, 'r').read()
            data = simplejson.loads(data_json)

            for item in data:
                Servidor.objects.get_or_create(
                    nome=item['nome'],
                    matricula=item['matricula']
                )