"""
Sistema de arquivos e navegação

Para fazer o uso de manipulação de arquivos do sistema operacional precisamos importar
e fazer uso do módulo os

os -> operating system - Sistema Operacional


# Fazer o import

import os

# getcwd() -> pega o current work directory - diretorio de trabalho corrente
# Retorna o path (caminho) absoluto

print(os.getcwd())  # /home/emanuel/PycharmProjects/aprendendoPython

# Para mudar o diretorio podemos utilizar o chdir()

os.chdir('..')  # Volta um diretorio
print(os.getcwd())  # /home/emanuel/PycharmProjects

os.chdir('..')  # Volta um diretorio
print(os.getcwd())  # /home/emanuel

os.chdir('..')  # Volta um diretorio
print(os.getcwd())  # /home

os.chdir('..')  # Volta um diretorio
print(os.getcwd())  # /

os.chdir('..')  # Volta um diretorio
print(os.getcwd())  # /

# Chegou na raiz não tem como ir mais

# Podemos checar se um diretorio é absoluto ou relativo

print(os.path.isabs('/home/emanuel'))  # É absoluto quando tem a raiz
# isabs() retorna ou true ou false

# OBS: para usuários windows
# se voce estiver usando um computador com windows
# tera que ter cuidado ao verificar diretorios.
# print(os.path.isabs('C:\\User\\emanuel'))


# Podemos identificar o sistema operacional com o modulo os

print(os.name)  # Posix (Linux e Mac), nt (Windows)


import os
import sys
# Podemos ter mais detalhes no sistema operacional
print(os.uname())
print(sys.platform)





print(os.getcwd())
os.chdir('..')

print(os.getcwd())
os.chdir('..')

print(os.getcwd())

res = os.path.join(os.getcwd(), 'PycharmProjects')
os.chdir(res)
print(os.getcwd())

# Veja que o os.path.join() recebe dois parametros, sendo o primeiro o diretorio atual e o segundo o
# diretorio que será juntado ao atual.


# Podemos listar os arquivos e diretorios com o listdir()
print(os.listdir('/etc'))

"""

# Fazer o import

import os

# Podemos listar os arquivos e diretorios com mais detalhes com o scandir()
scanner = os.scandir()

arquivos = list(scanner)

# print(arquivos)
# print(dir(arquivos[0]))
print(arquivos[0].inode())  # 12846324
print(arquivos[0].is_dir())  # é um diretorio?  False
print(arquivos[0].is_file())  # é um arquivo?  True
print(arquivos[0].is_symlink())  # É um link simbolico? False
print(arquivos[0].name)  # Nome do arquivo
print(arquivos[0].path)  # Caminho até o arquivo
print(arquivos[0].stat())  # Estatisticas sobre o arquivo

# OBS: Quando utilizamos a função scandir() nós precisamos fecha-lá, assim quando abrimos um arquivo.
scanner.close()


