"""
POO - Métodos Mágicos

Métodos mágicos, são todos os metodos que utilizam dunder.

Dunder > Double Underscore

dunder init -> __init__()
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas


dunder repr -> Representação do objeto
    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'


"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return self.titulo

    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'

    def __len__(self):
        return self.paginas

    def __del__(self):
        print('Um objeto foi deletado da memoria')

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'não posso multiplicar'


livro1 = Livro('Python Rocks', 'Geek University', 400)
livro2 = Livro('Inteligencia artificial com Python', 'Geek University', 350)

print(livro1)
print(livro2)
print(len(livro2))
print(len(livro1))

print(livro1 + livro2)
print(livro1 * 5)

