"""
Seek e Cursors

seek() -> é utilizada para movimentar o cursor pelo arquivo.

arquivo = open('texto.txt')

print(arquivo.read())

# seek() -> A função seek() é utilizada para movimentação do cursor pelo arquivo. Ela recebe um
# parametro que indica onde queremos colocar o cursor.

# Movimentando o cursor pelo arquivo com a função seek() -> Procurar
arquivo.seek(0)
print(arquivo.read())

arquivo.seek(22)
print(arquivo.read())


# readline() -> Função que lê o arquivo linha a linha (readline -> lê linha)

ret = arquivo.readline()

print(type(ret))
print(ret)
print(ret.split(' '))



# readlines() -> Retorna uma lista com todas as linhas como uma parte da lista
linhas = arquivo.readlines()
print(len(linhas))

# OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo
no disco do computador e o seu programa. Essa conexão é chamada de streaming. Ao finalizar
os trabalhos com o arquivo devemos fechar essa conexão. Para isso utilizamos a função close()

Passos para se trabalhar com um arquivo:

1 - abrir um arquivo

2 - trabalhar o arquivo

3 - Fechar o arquivo


# 1 - Abrir o arquivo:
arquivo = open('texto.txt')

# 2 - Trabalhar o arquivo:
print(arquivo.read())

print(arquivo.closed)  # False   Verifica se o arquivo esta aberto ou fechado

# 3 - Fechar o arquivo:
arquivo.close()
print(arquivo.closed)  # True

print(arquivo.read())

# OBS: Se tentarmos manipular o arquivo após o seu fechamento, teremos um ValueError

"""

# Podemos limitar a quantidade de cararcteres que vai ser lido no arquivo
arquivo = open('texto.txt')

print(arquivo.read(50))
# Imprime o resto
print(arquivo.read())
