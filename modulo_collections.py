"""
Módulo collections - Counter

Collections -> High performace Container Datetypes

Counter -> Recebe um iteravel como parametro e cria um objeto do tipo collections counter que é parecido com
com um dicionario, contendo como chave o elemento da lista passada como paramentro e como valor a quantidade
de ocorrencias desse elementos.



# Realizando o Import

from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iteravel aqui utilizamos uma lista
lista = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)
print(type(res))
print(res)

# Counter({1: 5, 2: 5, 3: 5, 4: 3, 5: 3, 45: 2, 66: 2, 43: 1, 34: 1})

# Veja que para cada elemento da lista o counter criou uma chave e colocou como valor a quantidade de ocorrencias.


# Exemplo 2

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})


# Exemplo 3

texto = '''
Montagem de oito páginas do Atlas Catalão do século XIV atribuído ao geógrafo e cartógrafo de Maiorca,
Abraão Cresques. Ao longo de sua vida, Cresques lidou com mapas, bússolas e relógios. Em 1375 recebeu
uma ordem de Pedro IV de Aragão para desenhar quatro mapas que deveriam cobrir tudo o que se conhece de leste
a oeste.
Surgiu então o Atlas Catalão que pode ser visto hoje na Biblioteca Nacional da França.
'''

palavras = texto.split()
#print(palavras)

res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrencias no texto
print(res.most_common(5))








Módulo Collections - Default Dict
# Recap Dicionarios

dicionario = {'curso': 'programação em python: essencial'}
print(dicionario)
print(dicionario['curso'])
print(dicionario['outro']) # KeyError


Default Dict -> Ao criar um dicionario utilizando-o, nós informamos um valor default,
podendo utilizar um lambda pra isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será criada
e o valor default será atribuido.

Obs: Lambdas são funções sem nome que podem ou não receber parametros de entrada e
retornar valores


# Fazendo import

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)
dicionario['curso'] = 'Programação em Python'
print(dicionario)

print(dicionario['outro']) # KeyError no dicionario comum, mas aqui não

print(dicionario)







Módulo Collections - Ordered Dict


# Em um dicionario, a ordem de inserção dos elementos não é garantida.
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(dicionario)

for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor}')

OrderedDict -> É um dicionario, que nos garante a ordem de inserção dos elementos.


# Fazendo o import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'Chave = {chave}: Valor = {valor}')


from collections import OrderedDict
# Entendendo a diferença entre Dict e Ordered Dict
# Dicionarios comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2) # True => ja que a ordem dos elementos não importa para o dicionario

# Ordered Dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2) # False -> já que a ordem dos elementos importam para o Ordered Dict






Módulo Collections - Named Tuple

# Recap Tupla

tupla = (num1 = 1, num2 = 2, num3 = 3)
print(tupla[1])
print(tupla)

Named Tuple -> São tuplas diferenciadas onde especificamos um nome para a mesma e tambem parametros

# Importando

from collections import namedtuple

# Precisamos definir o nome e parametros

# Forma 1 - declaração named tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - declaração named tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='Chow-chow', nome='ray')

# Acessando os dados

# Forma 1

print(ray)
print(ray[0])  # Idade
print(ray[1])  # Raça
print(ray[2])  # Nome


print('')

# Forma 2

print(ray.idade)
print(ray.raca)
print(ray.nome)

print(ray.index('Chow-chow'))  # MOSTRA O INDICE
print(ray.count('Chow-chow'))  # QUANTAS VEZES APARECE





Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performace


# IMPORTAR
from collections import deque

# Criando deques

deq = deque('geek')

print(deq)

# Adicionando elementos no deque

deq.append('y') # Adiciona no final
print(deq)

deq. appendleft('k') # ADICIONA NO COMEÇO DA LISTA
print(deq)

# Remover elementos

print(deq.pop()) # Remove e retorna o ultimo elemento
print(deq)
print(deq.popleft()) # Remove e retorna o primeiro elemento
print(deq)



"""
from collections import Counter
print(dir(Counter))


