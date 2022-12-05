"""
Lendo arquivos CSV

CSV - Comma Separeted Values - Valores Separados por virgula

 # Separador por virgula

 1, 2, 3, 4, 5, 6

 "Geek", "university", "python", "ciencia"

 # Separador por ponto e virgula

 1; 2; 3; 4; 5; 6

 "Geek"; "university"; "python"; "ciencia"

 # Separador por espaço

 1 2 3 4 5 6

 "Geek" "university" "python" "ciencia"


# Possivel de se trabalhar, mas não é o ideal (trabalhoso)

with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
    # print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)

O python possui duas formas diferentes para ler dados em arquivos CSV:
        - reader -> Permite que iteremos sobre as linhas do arquivo csv como listas;
        - DictReader -> Permite que iteremos sobre as linhas do arquivo csv como OrderedDicts;


# reader

from csv import reader

with open('lutadores.csv') as arquivo:
    leitor = reader(arquivo)
    next(leitor)  # Pular o cabecario
    for linha in leitor:
        # cada linha é uma lista
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centimetros')



# DictReader

from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor = DictReader(arquivo)
    for linha in leitor:
        # cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']}")


"""
# DictReader com outro separador

from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor = DictReader(arquivo, delimiter=',')
    for linha in leitor:
        # cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']}")


