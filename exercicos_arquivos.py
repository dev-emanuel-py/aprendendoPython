palavra = """
Hoje é dia de prova de AP  
A prova está muito facil
Vou tirar uma nota boa
1222
    """
with open('exercicio1.txt', 'w') as arquivo:
    arquivo.write(palavra)

with open('exercicio1.txt', 'r') as arquivo:
    invertido = arquivo.read()[::-1]

with open('exercicio2.txt', 'w') as arquivo:
    arquivo.write(invertido)



"""
        with open(nome, 'w') as dados:
            dados.write(str(codigo_vendedor) + '\n')
            dados.write(nome_vendedor + '\n')
            dados.write(str(valor_da_venda) + '\n')
            dados.write(mes + '\n')
            dados.write('\n')
            
            
            
            for i, nome in enumerate(nomes):
    print(nomes[i])
    print(codigos[i])
    print(valores_das_vendas[i])
    print(meses[i])
    print('')
"""