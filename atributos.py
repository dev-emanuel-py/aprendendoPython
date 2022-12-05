"""
POO - Atributos

Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos atributos
nós conseguimos representar computacionalmente os estados de um objeto.

Em python, dividimos os atributos em 3 grupos:
    - Atributos de instancia;
    - Atributos de Classe;
    - Atributos Dinamicos

## Atributos de instância: São atributos declarados dentro do método construtor.

# OBS: Metodo Construtor: é um metodo especial utilizado para a construção do objeto.

# Em java, uma classe lâmpada, incluindo seus atributos ficaria mais ou menos:

public class Lampada(){
    private int voltagem;
    private String cor;
    private Boolean ligada = false

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }

}
Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe é publico.
Ou seja pode ser acessado em todo o projeto.
Caso queiramos demostrar que determinado atributo deve ser tratado como privado, ou seja,
que deve ser acessado/utilizado somente dentro da propria classe onde está declarado,
utiliza-se __ duplo underscore no inicio de seu nome.

Isso é conhecido como  Name Mangling




# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não
# vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe.

# Exemplo


user = Acesso('user@gmail.com', '123456')

print(user.email)

# print(user.__senha)  # AttributeError

print(user._Acesso__senha)  # Temos acesso mas não deveriamos fazer esse acesso. (Name Mangling)

user.mostra_senha()
user.mostra_email()




# O que significa atributos de instância ?

# Significa que ao criamos instâncias/objetos de uma classe, todas as instancias
# terão estes atributos.

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')

user1.mostra_email()
user2.mostra_email()

# Atributos de classe

# Atributos de classe são atributos, que são declarados diretamentes na classe, ou seja,
# Fora do construtor. Geralmente já inicializamos um valor, e este valor é compartilhado entre
# Todas as instâncias da classe. Ou seja, ao invés de cada instancia da classe ter seus proprios
# Valores como é o caso dos atributos de instância, com os atributosde classe todas as instancias
# terão o mesmo valor para este atributo.


p1 = Produto('Play 4', 'video game', 2300)
p2 = Produto('XBox', 'video game', 4500)

print(p1.imposto)
print(p2.imposto)

print(p1.valor)  # Acesso Possível, mas incorreto de um atributo de classe
print(p2.valor)  # Acesso Possível, mas incorreto de um atributo de classe

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto)  # Acesso correto de um atributo de classe

print(Produto.contador)
print(p1.id)

# Em linguagens como java, os atributos conhecidos como atributos de classe aqui em Python
# são chamados de atributos estáticos;

"""

# Classe com atributo de instacia Publicos


class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos Públicos e Atributos Privados

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


# Refatorar a classe protudo


class Produto:

    # Atributo de classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


# Atributos dinamicos -> Um atributo de instancia que pode ser criado em tempo de execução.

# OBS: O atributo dinâmico será excusivo da instância que o criou.

p1 = Produto('Playstation 4', 'video game', 2300)
p2 = Produto('Arroz', 'mercearia', 5.99)

# Criando atributo dinâmico em tempo de execução

p2.peso = '5kg'  # Note que na classe Produto não existe o atributo peso

print(f'Produto: {p2.nome}, Descrição:{p2.descricao}, Valor:{p2.valor}, Peso:{p2.peso}')
# print(f'Produto: {p1.nome}, Descrição:{p1.descricao}, Valor:{p1.valor}, Peso:{p1.peso}')



# Deletando atributos
print(p1.__dict__)
print(p2.__dict__)

# print(Produto.__dict__)

del p2.peso
del p2.descricao
del p2.valor

print(p1.__dict__)
print(p2.__dict__)
