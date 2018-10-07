[![Build Status](https://travis-ci.org/royopa/debentures-scraper.svg?branch=master)](https://travis-ci.org/royopa/debentures-scraper)

# debentures-scraper

Projeto para captura dos preços unitários das debêntures do site www.debentures.com.br

## Instalando

```
> pip install --user pipenv
> pipenv shell
> python main.py
```

## Links

http://www.debentures.com.br/exploreosnd/consultaadados/emissoesdedebentures/puhistorico_f.asp

http://www.debentures.com.br/exploreosnd/consultaadados/emissoesdedebentures/puhistorico_e.asp?op_exc=False&ativo=AALR11++++&dt_ini=&dt_fim=&Submit.x=34&Submit.y=13

## Download dos arquivos

O programa [main.py](main.py) faz o download de todas os arquivos de preços unitários diarios das debêntures registradas no site.