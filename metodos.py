"""
POO - Métodos

- Métodos (funções) -> Representamos os comportamentos do objeto. Ou seja, as ações
que este objetos pode realizar no seu sistema.

Em python, dividimos os métodos em 2 grupos: Métodos de instancia e
métodos de classe.

# Métodos de instancia

# O método dender init __init__ é um metodo especial chamado de construtor e
sua função é construir o objeto a partir da classe.

OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)

Obs: Os métodos/funções dunder em Python são chamados de métodos mágicos.

ATENÇÃO! Por mais que possamos criar nossas proprias funções utilizando dunder (underline no início e no fim)
não é aconselhado. Python possui varios métodos com está forma e nomeclatura e pode ser que mudemos o comportamento
dessas funções mágicas internas da linguagem. Então, evite ao máximo. De preferência nunca o faça.

Métodos são escritos em letras minusculas. Se o nome for composto, o nome terá palavras separadas por underline.






p1 = Produto('Playstation 4', 'video game', 2300)
print(p1.desconto(50))

print(Produto.desconto(p1, 40))  # self, desconto


user1 = Usuario('Emanuel', 'Flavio', 'emanuel@gmail.com', '123456')
user2 = Usuario('Everton', 'Flavio', 'everton@gmail.com', '654321')

print(user1.nome_completo())
print(user2.nome_completo())

print(Usuario.nome_completo(user1))
print(f'Senha user 1: {user1._Usuario__senha}')  # Acesso de forma errada de um atributo de classe

print(f'Senha user 2: {user2._Usuario__senha}')  # Acesso de forma errada de um atributo de classe








nome = input('informe o nome')
sobrenome = input('informe o sobrenome')
email = input('informe o email')
senha = input('Informe a senha')
confirma_senha = input('Confirme a senha:')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere...')
    exit(1)

print('usuario criado com sucesso')

senha = input('Informe sua senha para o acesso:')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('acesso negado')

print(f'Senha User Criptografada: {user._Usuario__senha}')  # Acesso errado





# Métodos de classe

user1 = Usuario('Emanuel', 'Flavio', 'emanuel@gmail.com', '1234')
user2 = Usuario('Everton', 'Silva', 'everton@gmail.com', '4321')

Usuario.conta_usuarios()  # Forma correta (Via nome da classe)
user1.conta_usuarios()  # Possível, mas incorreta

# Obs: Os metodos de instancia só são criados quando for preciso fazer acesso a atributos de instancia
# Obs: Os métodos de classe não fazem acesso aos atributos de instancia

# OBS: Métodos de classe em python são conhecidos como métodos estaticos em outras linguagens



user = Usuario('Emanuel', 'Flavio', 'emanuel@gmail.com', '1234')

print(user._Usuario__gera_usuario())  # Acesso, de forma ruim...

"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        ContaCorrente.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna um valor do produto com desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


from passlib.hash import pbkdf2_sha256 as crp


class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'temos {cls.contador} usuario(s) no sistema')

    @classmethod
    def ver(cls):
        print('teste')

    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = crp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if crp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


# Método estático

print(Usuario.contador)
print(Usuario.definicao())

user = Usuario('Emanuel', 'Flavio', 'emanuel@gmail.com', '1234')

print(user.contador)
print(user.definicao())

