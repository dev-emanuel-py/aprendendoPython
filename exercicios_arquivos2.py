import os

def menu():
    print('1 - Criar o arquivo de dados')
    print('2 - Incluir um determinado registro no arquivo')
    print('3 - Excluir um determinado vendedor no arquivo')
    print('4 - Alterar o valor de uma venda no arquivo')
    print('5 - Imprimir os registros na saida padrão')
    print('6 - Excluir o arquivo de dados')
    print('7 - Finalizar o programa')


menu()
selecionar = int(input('Digite sua opção: '))
codigos = []
nomes = []
valores_das_vendas = []
meses = []
while selecionar != 7:

    if selecionar == 1:
        os.mknod('dados.txt')
        menu()

    if selecionar == 2:
        codigo_vendedor = int(input('Digite o codigo do vendedor: '))
        nome_vendedor = input('Digite o nome do vendedor: ')
        valor_da_venda = int(input('Digite o valor da venda: '))
        mes = input('Digite o mes: ')
        codigos.append(codigo_vendedor)
        nomes.append(nome_vendedor)
        valores_das_vendas.append(valor_da_venda)
        meses.append(mes)

    if selecionar == 3:
        vendedor_excluido = input('Qual o vendedor que será excluido: ')
        for i, nome in enumerate(nomes):
            if nome == vendedor_excluido:
                nomes.remove(nomes[i])
                codigos.remove(codigos[i])
                valores_das_vendas.remove(valores_das_vendas[i])
                meses.remove(meses[i])

    if selecionar == 4:
        vendedor_alteracao = input('Qual o vendedor que mudará o valor da venda: ')
        for i, nome in enumerate(nomes):
            if nome == vendedor_alteracao:
                novo_valor = int(input(f'Novo valor de venda de {nome}: '))
                valores_das_vendas[i] = novo_valor

    if selecionar == 5:
        for i, nome in enumerate(nomes):
            print(nomes[i])
            print(codigos[i])
            print(valores_das_vendas[i])
            print(meses[i])
            print('')

    if selecionar == 6:
        os.remove('dados.txt')

    menu()
    selecionar = int(input('Digite sua opção: '))

with open('dados.txt', 'w') as dados:
    for i, nome in enumerate(nomes):
        dados.write('Codigo: ' + str(codigos[i]) + '\n')
        dados.write('Nome: ' + nomes[i] + '\n')
        dados.write('Valor: ' + str(valores_das_vendas[i]) + '\n')
        dados.write('Meses: ' + meses[i] + '\n')
        dados.write('\n')
