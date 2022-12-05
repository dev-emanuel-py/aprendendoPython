"""
Sistema de arquivos - manipulação

# Descobrindo se um arquivo ou diretorio existe

# Arquivo
print(os.path.exists('fruta.txt'))  # True
print(os.path.exists('arquivo.txt'))  # False

# Diretorio

# Paths relativos
print(os.path.exists('geek/university'))  # True
print(os.path.exists('geek'))  # True
print(os.path.exists('geek/university/geek3.py'))  # True
print(os.path.exists('outro'))  # False


# Paths absolutos
print(os.path.exists('/home/emanuel/PycharmProjects/aprendendoPython/'))  # True
print(os.path.exists('/home/emanuel/Imagens/images.jpeg'))  # True


# Criando arquivos

# Forma 1
open('arquivo.txt', 'w').close()

# Forma 2
open('arquivo_teste.txt', 'a').close()

# Forma 3
with open('arquivo_teste2.txt', 'w') as arquivo:
    pass


# Forma 4 - melhor forma
os.mknod('arquivo_teste3.txt')
os.mknod('/home/emanuel/PycharmProjects/aprendendoPython/teste_3.txt')

# Se voce estiver utilizando no MacOs, pode haver um erro de PermissionError
# Criando um arquivo via mknod() se o arquivo já existir teremos o erro FileExistsError


# Criando diretorios - unicos (Um a um)

# Path Relativo
os.mkdir('templates')

# A função mkdir() cria um diretorio se este não existir. Caso exista, teremos FileExistsError

# Path Absoluto
os.mkdir('/home/emanuel/PycharmProjects/aprendendoPython/templates')

os.mkdir('etc/templates')
# OBS: Se não tivermos permissão para criar o diretorio termos um PermissionError

# Criando varios diretorios (árvore de diretórios)

# Forma 1
os.mkdir('templates')
os.mkdir('templates/geek')
os.mkdir('templates/geek/university')


# Forma 2
os.makedirs('templates/geek/university')

# OBS: Se já existir, teremos um FileExistsError

os.makedirs('templates2/novo/novo2', exist_ok=True)


# Renomear arquivos e diretorios

# os.rename('Geek2/nome2', 'Geek3')

# Obs: se o diretorio não existir teremos um FileNotFoundError
# Obs: Se o diretorio que queremos renomear não estiver vazio, teremos um OSError

# Arquivos
#os.rename('Geek2/novo/novo2/os.txt', 'Geek2/novo/novo2/geek.txt')

os.rename('fruta.txt', 'cesta.txt')


# Removendo arquivos

# Atenção! Cuidado com os comandos de deleção. Ao deletarmos um arquivo ou diretorio,
# eles não vão para lixeira. Eles somem.

os.remove('arquivo.txt')

# Obs: Se voce estiver no windows e o arquivo que você for deletar estiver em uso, teremos um erro.
# Caso o arquivo não exista teremos o FileNotFoundError

# Se for informado um diretorio ao inves de um arquivo, teremos um IsADirectoryError


# Removendo diretorios Vazios

os.rmdir('templates')

# Se o diretoiro tiver qualquer conteudo teremos um OSError

# OBS: se o diretorio não existir teremos um FileNotFoundError




# Removendo uma arvore de arquivos

for arquivo in os.scandir('Geek2'):
    print(f'{arquivo.name}')
    if arquivo.is_file():
        os.remove(arquivo.path)




# Podemos remover uma arvore de diretorios vazios

os.removedirs('Geek2/kfjkdhn')

# Se alguns dos diretorios contiver arquivos ou outros diretorios, o processo para.


import os

# ATENÇÃO: Ao remover arquivos e diretorios com python eles não vão para a lixeira. Eles vão embora !

# Importando a biblioteca send2trash (Envia arquivos e diretorios para a lixeira)

from send2trash import send2trash

os.remove('cesta2.txt')  # Não vai para a lixeira. É deletado imediatamente

send2trash('cesta.txt')  # Vai para a lixeira. Pode ser restaurado

# Se o arquivo não existir teremos OSError


# Enviando diretorios para a lixeira
from send2trash import send2trash

send2trash('teste')



# Trabalhando com arquivos e diretórios temporarios

import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretorio temporario em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University \n')
    input()

# Estamos criando um diretorio temporario abrindo o mesmo e dentro dele criando um arquivo para escrevermos um texto
# No final usamos um input só para mantermos
# os arquivos temporarios 'vivos' dentro do bloco with.

# OBS: possivelmente, o codigo acima não irá funcionar se voce estiver usando o windows.
# por conta desse sistema trabalhar de forma diferente com arquivos
# temporarios


# Criando arquivos temporarios

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University \n')
    tmp.seek(0)
    print(tmp.read())

# Em arquivos temporarios so conseguimos escrever bits. Por isso utilizamos
# b''



sem o bloco with

arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University \n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()



# Trabalhando com arquivos e diretórios temporarios

import os
import tempfile

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University\n')
print(arquivo.name)
print(arquivo.read())
input()
arquivo.close()

# Documentação do modulo os
https://docs.python.org/3/library/os.html?highlight=os#module-os

"""


