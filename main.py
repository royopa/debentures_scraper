# -*- coding: utf-8 -*-
import csv
import time
import os
import wget
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup


def get_links():
    url_base = 'http://www.debentures.com.br/exploreosnd/consultaadados/emissoesdedebentures/'
    url = url_base+'puhistorico_f.asp'
    res = requests.get(url)

    while res.status_code != 200:
        res = requests.get(url)

    soup = BeautifulSoup(res.text,"html.parser")
    select = soup.find("select", {"name":"ativo"})

    urls = []
    for option in select.find_all('option'):
        ativo = option['value'].strip()
        
        if len(ativo) < 6:
            continue
        
        url_download = url_base + 'puhistorico_e.asp?op_exc=False&dt_ini=&dt_fim=&Submit.x=34&Submit.y=13&ativo='+ativo+'++++'
        urls.append({'ativo': ativo,'url':url_download})

    return urls


def main():
    directory = 'downloads'
    if not os.path.exists(directory):
        os.makedirs(directory)
    urls = get_links()
    for url in urls:
        print(' Baixando arquivo do ativo', url['ativo'])
        name_file = url['ativo']+'.csv'
        print(name_file)
        path_file = os.path.join('downloads', name_file)
        if not os.path.exists(path_file):
            wget.download(url['url'], path_file)


if __name__ == '__main__':
    main()