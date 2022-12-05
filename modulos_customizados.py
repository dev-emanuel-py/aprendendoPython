"""
Módulos customizados

Como módulos python nada mais são do que arquivos python, então todos os arquivos que criamos
neste curso são modulos python prontos para serem utilizados.



# Importando uma função especifica do nosso módulo

from funcoes_com_parametro import soma_impares_certo

print(soma_impares_certo([1, 2, 3, 4, 5]))



# Importando todo o modulo ( Temos acesso a todos os elementos do modulo)
import funcoes_com_parametro as fcp

# Estamos acessando e imprimindo uma variavel contida no módulo
print(fcp.lista)

print(fcp.soma_impares_certo(fcp.lista))
"""

from map import cidades

print(cidades)

