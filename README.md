Python Sul 2020
============

[pythonsul.org](http://pythonsul.org)

Projeto Pelican para criação so site da Python Sul 2020!

# Ambiente
```shell
git clone git@github.com:pythonsul/pythonsul2020-site.git;
cd pythonsul2020-site
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Rodar
```shell
source .venv/bin/activate
invoke reserve
```

# Configuração
 - python decouple para configurar a url.

# Deploy
```shell
[dentro da env]$ invoke gh-pages
```