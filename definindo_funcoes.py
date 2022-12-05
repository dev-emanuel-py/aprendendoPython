"""
Definindo funções

- Funções são pequenas partes de codigo que realiza tarefas especificas;
- Pode ou não receber entrada de dados e retornar uma saída de dados;
- Muito uteis para executar procedimentos similares por repetidadas vezes;

Obs: se voce escrever uma função que realiza varias tarefas dentro dela;
é bom fazer uma verificação para que a função seja simplificada.

Já utilizamos várias funções desde de que iniciamos este curso:
- print()
- len()
- max()
- min()
- count()
- e muitas outras;

"""

# Exemplo de utilização de funções

#cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando uma função integrada (Built-in) do Python print()
#print(cores)

#curso = 'Programação em python essencial'

#print(curso)

#cores.append('roxo')
#print(cores)

# curso.append('mais dados...') # AttributeError
# print(curso)

#cores.clear()
#print(cores)

# print(help(print))
# DRY - Don't Repeat Yourself - Não repita seu você mesmo / não repita seu codigo
# Mas então, como difinir funções ?

"""
Em python, a forma geral de definir uma função é:

def nome_da_funcao(paramentros_de_entrada):
    bloco_da_funcao
    
Onde:
nome_da_funcao -> sempre, com letras minusculas, e se for nome composto, separado por underline(Snake Case)
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separados por virgula, podendo ser opcionais ou não;
bloco_da_funcao -> Tambem chamado de corpo da funcao ou implementação, é onde o processamento da funcao acontece.
Neste bloco, pode ter ou não retorno da função.

Obs: Veja para que definir uma função, utilizamos a palavra reservada 'def' informando ao python que
estamos definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos ':' que é utilizado 
em python para definir blocos.  
"""

# Definindo a primeira função
# Definição


def diz_oi():
    print('Oi !')

"""
Obs:

1 - Veja que, dentro das nossas funções podemos utilizar outras funções;
2 - Veja que nossa função só executa 1 tarefa, ou seja, a unica coisa que ela faz é dizer oi;
3 - Veja que está função não recebe nenhum parametro de entrada;
4 - Veja que esta função não retorna nada;
"""

# Utilizando funções

# Chamada de execução
# diz_oi()

"""
Atenção:

Nunca esqueça de utilizar o parenteses ao execultar uma função.

Exemplo:

# Errado
diz_oi

# Certo
diz_oi()

# Errado 
diz_oi ()

"""

# Exemplo 2

def cantar_parabens():
    print('parabens pra voce')
    print('nesta data querida')
    print('muitas felicidades')
    print('muitos anos de vida')
    print('viva o aniversariante !')

# for i in range(4):
#     cantar_parabens()

# Em Python, podemos inclusive criar variáveis do tipo de uma função e executar esta função atraves da variavel


canta = cantar_parabens

canta()
