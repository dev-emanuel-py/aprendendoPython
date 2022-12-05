"""
Modos de abertura de arquivos

r -> Abre para leitura - padrão
w -> abre para escrita - sobrescreve caso o arquivo ja exista
x -> abre para escrita, somente se o arquivo não existir. Caso o arquivo exista, gera FileExistsError.
a -> abre para escrita, adicionando o conteudo ao final do arquivo.
+ -> abre para o modo de atualização: Leitura e escrita. (Temos o controle do cursor)

# obs: abrindo no modo 'a' -> append, se o arquivo não existir será criado. Caso exista, o novo conteudo
será adicionado ao final do arquivo SEMPRE. Com o modo 'a' não controlamos o cursor.




http://docs.python.org/3/library/functions.html#open


# Exemplo x

try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteudo 2. \n')
except FileExistsError:
    print('Arquivo já existe')


# Exemplo a

with open('fruta.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
"""
# Exemplo r+

with open('outro.txt', 'r+') as arquivo:
    arquivo.seek(0)
    arquivo.write('adicionada \n')
    arquivo.write('Nova Linha. \n')
    arquivo.write('Mais uma linha. \n')






