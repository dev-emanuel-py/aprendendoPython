"""
O bloco with

passos para se trabalhar com arquivos

# 1 - Abrimos o arquivo
# 2 - Manipulamos o arquivo
# 3 - Fechamos o arquivo

O Bloco wuth é utilizado para criar um contexto de trabalho onde os recursos
utilizados são fechados após o bloco with.


"""

# O bloco with - Forma pythonica de manipular arquivos

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)  # False

# print(arquivo.read())  # ValueError: I/O operation on closed file.

print(arquivo.closed)  # True
