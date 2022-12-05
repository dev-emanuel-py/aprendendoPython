"""
Decoradores (decorators)

O que são decorators?

- Decorators são funções
- Decorators envolvem outras funções e aprimoram seus comportamentos
- Decorators tambem são exemplos de higher order functions
- Decorators tem uma sintaxe propria, usando "@" (Syntact Sugar / Acucar Sintatico)


/-------------------------------------/
/         Funções Decorator           /
/-------------------------------------/


---------------------------------------
/-------------------------------------/
/       /   Função decorada    /      /
/-------------------------------------/
---------------------------------------




# Decorators como funções (sinataxe não recomendada / Sem acucar sintatico)


def seja_educado(funcao):
    def sendo():
        print('Foi um prazer te conhecer! ')
        funcao()
        print('tenha um otimo dia! ')
    return sendo


def saudacao():
    print('seja bem vindo a geek university')

# Testando 1

# saudacao()


teste = seja_educado(saudacao)

teste()

# Testando 2

def raiva():
    print('EU TE ODEIO')


raiva_educada = seja_educado(raiva)

raiva_educada()






# Decorators com Syntax sugar (Acucar sintatico)


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer te conhecer! ')
        funcao()
        print('Tenha um exelente dia! ')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('meu nome é pedro')


# Testando

apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormir...')


dormir()

"""

"""
/-----------------------------------------------/
/ Home   / servicos / Produtos / administrativo /
-------------------------------------------------

http:// www.suaempresa.com.br/home
http:// www.suaempresa.com.br/servicos
http:// www.suaempresa.com.br/produtos
http:// www.suaempresa.com.br/admin


# Não é um codigo funcional

def checa_login(request):      # DECORATOR FUNCTION
    if not request.usuario:
        redirect('http:// www.suaempresa.com.br')
        

def home(request):
    return 'Pode acessar home'
    
def servicos(request):
    return 'Pode acessar servicos'

def produtos(request):
    return 'Pode acessar produtos'

@checa_login                     # DECORATOR
def admin(request):
    return 'Pode acessar admin'
"""

# Obs: Não confunda decorator com decoration functions

