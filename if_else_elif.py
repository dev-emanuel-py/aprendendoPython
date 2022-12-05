"""
Estruturas condicionais
if(Se), else, elif
"""

idade = 26

"""
# Estrutura condicional if em C:

if(idade < 18){
    printf("menor de idade");
}
else if(idade == 18){
printf("Tem 18 anos")
}
else{
printf("maior de idade")
}
"""

"""
# Estrutura condicional if em Java:

if(idade < 18){
    System.out.println("menor de idade");
}
else if(idade == 18){
    System.out.println("Tem 18 anos")
}
else{
    System.out,println("maior de idade")
}
"""

if idade < 18:
    print('Menor de Idade')
elif idade == 18:
    print('Tem 18 anos')
elif idade == 26:
    print('Tem 26 anos')
else:
    print('Maior de Idade ')
