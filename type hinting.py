# def cumprimentos(nome: str) -> str:
#    return f'Olá, {nome}'
#
#
# print(cumprimentos('emanuel'))


def cabecacho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecacho('geek university'))

print(cabecacho('geek university', False))

print(cabecacho('geek university', alinhamento='geek'))


# correto

texto: str

# Incorreto

texto:str
texto : str

# correto

) -> str
)->str
) ->str

# correto

alinhamento: bool = True

# Incorreto

alinhamento:bool=True
