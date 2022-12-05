"""
StringIO

Atenção: para ler ou escrever dados em arquivos do sistema operacional o software precisa
ter permissão:
    - Permissão de leitura -> para ler o arquivo.
    - Permissão de escrita -> para escrever no arquivo.

StringIO -> Utilizado para ler e criar arquivos em memoria.


"""

# Primeiro fazemos o import

from io import StringIO

mensagem = 'Esta é apenas uma string normal'

# Podemos criar um arquivo em memoria já com uma string inserida ou mesmo vazio para inserimos texto depois

arquivo = StringIO(mensagem)
# arquivo = open('arquivo.txt', 'w')  # são semelhantes

# Agora com o arquivo, podemos utilizar tudo que ja sabemos.
print(arquivo.read())

# Escrevendo outros textos
arquivo.write(' Outro texto ')

# Podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())
