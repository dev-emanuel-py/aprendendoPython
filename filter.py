"""

Filter

filter() -> serve para filtrar dados de uma determinada coleção.


# Biblioteca para trabalhar com dados estatísticos
import statistics

# dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a finção mean()
media = statistics.mean(dados)
print(media)

# OBS: Assim como a função map(), a filter() recebe dois parametros, sendo
# uma função e um iterável.

res = filter(lambda x: x > media, dados)
print(list(res))

# Obs: Assim como na função map(), apos serem utilizados os dados do filter() eles são excluidos da memoria
print(f'Novamente: {list(res)}')




paises = ['', 'Argentina', '', 'Brasil', '', 'Chile', '', 'Colombia', '', '', 'Equador', '', '', 'Velezuela']

print(paises)

res = filter(None, paises)
print(list(res))



paises = ['', 'Argentina', '', 'Brasil', '', 'Chile', '', 'Colombia', '', '', 'Equador', '', '', 'Velezuela']

print(paises)

# res = filter(lambda pais: len(pais) > 0, paises)
# res = filter(None, paises)
res = filter(lambda pais: pais != '', paises)
print(list(res))

# 3 formas de fazer
# res = filter(lambda pais: len(pais) > 0, paises)
# res = filter(None, paises)
# res = filter(lambda pais: pais != '', paises)



# A diferença entre map() e filter() é:

# map() -> Recebe dois parametros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento
# do iteravel

# filter() -> Recebe dois parametros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de
# acordo com a função






# Exemplo mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Eu vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

# Filtrar os usuarios que estão inativos no twitter

# Forma 1
# inativos = list(filter(lambda user: len(user['tweets']) == 0, usuarios))

# Forma 2
inativos = list(filter(lambda user: not user['tweets'], usuarios))
print(inativos)


"""


# Combinar filter() e map()

nomes = ['vanessa', 'ana', 'maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde de que cada nome tenha menos de 5 caracteres

res = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(res)
