"""
Escrevendo em arquivos CSV

reader() (leitor)
writer() (escritor)

writerow() -> Escreve uma linha




from csv import writer

with open('filmes.csv', 'w') as arquivo:
    escritor = writer(arquivo)
    filme = None
    escritor.writerow(['titulo', 'genero', 'duracao'])
    escritor.writerow([])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('informe o gereno do filme: ')
            duracao = input('Informe a duração do filme (em minutos): ')
            escritor.writerow([filme, genero, duracao])

"""

# DictWriter

# Obs: as chaves do dicionario devem ser as mesmas utilizadas como cabeçalho.

from csv import DictWriter

with open('filmes.csv', 'w') as arquivo:
    cabecalho = ['titulo', 'genero', 'duracao']
    escritor = DictWriter(arquivo, fieldnames=cabecalho)
    escritor.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o filme: ')
        if filme != 'sair':
            genero = input('Informe o genero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor.writerow({"titulo": filme, "genero": genero, "duracao": duracao})

