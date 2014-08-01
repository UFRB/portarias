# -*- coding: utf-8 -*-
from django import forms

class ImportarServidores(forms.Form):

    arquivo_link = forms.URLField(label='Link do Arquivo')