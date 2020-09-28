# -*- coding: utf-8 -*-
import csv
import os
import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup

import utils


def get_links():
    url_base = 'http://www.debentures.com.br'
    url_pu = f'{url_base}/exploreosnd/consultaadados/emissoesdedebentures/'
    url = url_pu+'puhistorico_f.asp'
    res = requests.get(url)

    while res.status_code != 200:
        res = requests.get(url)

    soup = BeautifulSoup(res.text, "html.parser")
    select = soup.find("select", {"name": "ativo"})

    urls = []
    for option in select.find_all('option'):
        ativo = option['value'].strip()

        if len(ativo) < 6:
            continue

        ativo = ativo.replace(' ', '+')

        today = datetime.today()

        url_compl = '/exploreosnd/consultaadados/emissoesdedebentures/'
        url = f'{url_base}{url_compl}'
        url = f'{url}puhistorico_e.asp?'
        url = f'{url}op_exc=False&dt_ini=&Submit.x=34&Submit.y=13'
        url = f"{url}&dt_fim={today.strftime('%d/%m/%Y')}&ativo={ativo}++++"
        urls.append({'ativo': ativo, 'url': url})

    return urls


def main():
    utils.prepare_download_folder('downloads')

    urls = get_links()
    for index, url in enumerate(urls):
        name_file = url['ativo']+'.csv'
        path_file = os.path.join('downloads', name_file)
        print(' Baixando arquivo do ativo', url['ativo'], name_file)
        utils.download(url['url'], None, path_file)
        time.sleep(1)

        if index % 500 == 0:
            print('Aguardando 30 segundos, para evitar timeout')
            time.sleep(30)


if __name__ == '__main__':
    main()
