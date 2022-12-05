"""
Módulos Externos

Utilizamos o gerenciador de pacotes chamado pip - Python Installer Packge

Voce pode conhecer todos os pacotes externos oficiais em: https://pypi.org

instalando um modulo:
pip install nome-do-modulo


# Instalando o pacote colorama

pip install colorama

colorama -> é utilizado para a impressão de textos coloridos no terminal.

from colorama import Fore, Back, Style, init

print(Fore.BLACK + 'some red text')
print('nem')
print(Back.BLUE + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
"""

import pydf
pdf = pydf.generate_pdf('<h1>Geek University</h1><br/><br/><strong>Emanuel</strong>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)

from colorama import Fore, Back, Style, init

