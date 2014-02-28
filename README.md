portarias
=========

Esta é uma aplicação Django para publicação de Portarias, a qual possibilita que vários funcionários emitam portarias sem correr o risco de ter numeração duplicada. Além disso, disponibiliza uma interface web para que as pessoas consultem as portarias publicadas.

Este é um projeto da [UFRB](http://ufrb.edu.br/).

Instruções
---------

Instale o _portarias_ e adicione as seguintes apps em `INSTALLED_APPS` no seu `settings.py`:

```
    'portaria',
    'filer',
    'easy_thumbnails',
```

Já no `urls.py`, adicione:

```
    url(r'^', include('portaria.urls', namespace='portaria')),
```

