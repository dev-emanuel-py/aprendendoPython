def cabecacho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, ' ')


print(cabecacho('geek university'))

print(cabecacho('geek university', False))

print(cabecacho('geek university', alinhamento=True))
