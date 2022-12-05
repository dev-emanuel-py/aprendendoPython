"""
Escrevendo em arquivos

# OBS: Ao abrir um arquivo para leitura não podemos realizar a escrita nele. Apenas ler.
Da mesma forma, se abrimos um arquivo para escrita, não podemos lẽ-lo, somente escrever nele.

# OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

# Obs: Para escrevermos dados em um arquivo , apos abrir o arquivo utilizamos a função write().
Esta função recebe uma string como parametro, caso contrario teremos um TypeError.
TypeError: write() argument must be str, not int

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado,
caso ele ja exista, o anterior será apagado e um novo será criado. Dessa forma, todo
o conteudo no arquivo anterior é perdido.

"""

# Exemplo de escrita - modo 'w' - write(escrita)- Forma Pythonica

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Novos dados. \n')
    arquivo.write('Outros podemos colocar quantas linhas quisermos \n')
    arquivo.write('mas essa é a ultima linha é a ultima linha')


# Forma tradicional de escrita

arquivo = open('mais.txt', 'w')

arquivo.write('Um texto qualquer. \n')
arquivo.write('Mais um texto')

arquivo.close()


# Outro exemplo
with open('geek.txt', 'w') as arquivo:
    arquivo.write('Geek ' * 1000)

# Outro exemplo
with open('fruta.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

