"""
Pacotes

Módulo -> é apenas um arquivo python que pode ter diversas funções para utilizarmos;

Pacote -> é apenas um diretório contendo uma coleção de módulos;

OBS: Nas versoes 2.x no python, um pacote python deveria conter dentro dele um
arquivo chamado __init__.py

Nas versoes do python 3.x, não é mais obrigatoria a utilização deste arquivo, mas
normalmente ainda é utilizado para manter compatibilidade.




from geek import geek1, geek2

from geek.university import geek3, geek4    # Importando subpacotes

print(geek1.funcao1(2, 5))
print(geek1.pi)
print(geek2.curso)
print(geek2.funcao2())
print(geek3.funcao3())
print(geek4.funcao4())



"""

# Importando a função de um modulo
from geek.geek1 import funcao1
# Importando a funcão de um modulo de um subpacote
from geek.university.geek4 import funcao4

print(funcao4())
print(funcao1(6, 9))




