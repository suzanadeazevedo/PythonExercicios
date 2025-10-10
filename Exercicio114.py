"""Crie um código em Python que teste se o site pudim está acessível pelo computador usado"""

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')

except:
    print(f'\n\033[0;31m!ERRO! Não foi possivel acessar o site PUDIM .\033[m')
else:
    print(f'\n\033[0;32mFoi possivel acessar o site PUDIM.\033[m')
    