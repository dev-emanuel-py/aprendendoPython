"""
Dicionarios

OBS: em algumas linguagens de programação, os dicionarios Python são conhecidos
por mapas.

Dicionarios são coleções do tipo chave/valor

Dicionarios são representados por chave {}.

print(type({}))

    obs: Sobre dicionarios
        -   Chave e valor são separados por dois pontos 'chave:valor';
        -   Tanto chave quanto valor podem ser de qualquer tipo de dado;
        -   POdemos misturar tipos de dados;

# Criação de dicionarios

# forma 1 (Mais comum)

paises = {'br': 'brasil', 'eua': 'Estados Unidos', 'py': 'paraguai'}
print(paises)
print(type(paises))

# Forma 2 (menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='paraguai')
print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
# print(paises['ru'])

# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2 - Acessando via get - Recomendada

print(paises.get('br'))
print(paises.get('ru '))

# Caso o get não encontre objeto com o valor informado será retornado o valor None e não será gerado KeyError.

pais = paises.get('ru')

if pais:
    print(f'encontrei o pais {pais}')
else:
    print('Não encontrei o pais')


Obs: Podemos definir um valor padão para caso não encontremos o objeto com a chave informada
pais = paises.get('py', 'Não encontrado')

print(f'encontrei o pais {pais}')

# podemos verificar se determinada chave se encontra em um dicionario

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']



# Podemos utilizar qualquer tipo de dado(int, float, string, boolean), inclusive lista, tupla, dicionario, como chave
# de dicionario.

# Tuplas por exemplo são bastante interessantes para serem usadas como chaves de dicionario pois são imutaveis

localidades = {
    (35.2895, 39.6917): 'Escritorio em Toquio',
    (40.6225, 74.3947): 'Escritorio em Nova York',
    (22.7822, 59.3915): 'Escritorio em São Paulo'
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionario

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# forma 1

receita['abr'] = 350
print(receita)

# forma 2

novo_dado = {'mai': 500}

receita.update(novo_dado) # receita.update({'mai': 500})

print(receita)

# Atualizando dados em um dicionario

# Forma 1

receita['mai'] = 550

print(receita)

# forma 2

receita.update({'mai': 600})

print(receita)

# Conclusão 1: a forma de adicionar novos elementos ou atualizar dados em um dicionario é a mesma.
# Conclusão 2: Em dicionarios, NÃO PODEMOS TER CHAVES REPETIDAS.


# COMO REMOVER DADOS DE UM DICIONARIOS

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

# Forma 1 - Mais Usado
removido = receita.pop('mar')
print(removido)

print(receita)
# Obs 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado.
# Obs 2: Ao removermos um objeto o valor desse objeto é sempre retornado.

# Forma 2
del receita['fev']

print(receita)

# se a chave não existir será gerado um KeyError
# Neste caso o valor removido não é retornado.




# Imagine que voce tem um comercio eletronico, onde temos um carrinho de compras na qual adicionamos produtos.

Carrinho de compras:
    Produto 1:
        -   nome
        -   quantidade
        -   preço
    Produto 2:
        -   nome
        -   quantidade
        -   preço

#  1 - Poderiamos criar uma lista para isso ?  sim

carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# teriamos que saber qual é o indice de cada informação no produto.

# 2 - Poderiamos utilizar uma tupla pra isso? Sim

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 2', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# teriamos que saber qual é o indice de cada informação no produto.

# Poderiamos utilizar o dicionario para isso? Sim

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# podemos ter a certeza sobre cada informação


# Metodos de dicionarios.

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionario (Zerar dados)

d.clear()

print(d)



# COPIANDO UM DICIONARIO PARA OUTRO

# FORMA 1 # Deep Copy

novo = d.copy()

print(novo)

novo['d'] = 4

print(d)
print(novo)
print(type(novo))


# Forma 2 # Shallow Copy

novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)

"""

# Forma não usual de criação de dicionarios

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')

print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parametros: um iteravel e um valor.
# Ele vai gerar para cada valor do iteravel uma chave e irá atribuir a esta chave o valor informado

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)

