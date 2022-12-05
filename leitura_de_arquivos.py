"""
Leitura de arquivos

Para o conteúdo de um arquivo em python, utilizamos a função integrada open(),
que literalmente significa abrir.

open() -> Na forma mais simples de utilização nos poassamos apenas um parametro
de entrada, que neste caso é o caminho do arquivo a ser lido. Essa função retorna
um _io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

# OBS: Por padrao, a função open() abre o arquivo para leitura. Este arquivo
deve existir, ou então teremos o erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='UTF-8'>

mode = 'r' -> Modo de leitura. r -> read() -> ler



"""

# Exemplo

arquivo = open('texto.txt')

# print(arquivo)
# print(type(arquivo))

# Para ler o conteudo de um arquivo, apos sua abertura, devemos utilizar a função read()

ret = arquivo.read()

print(type(ret))

print(ret)

# print(arquivo.read())

# O python utiliza um recurso para trabalhar com arquivis chamado cursor. Esse cursor,
# funciona como o cursor quando estamos escrevendo.

# print(arquivo.read())

# OBS: A função read() lê todo o conteudo do arquivo.




