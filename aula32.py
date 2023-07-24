"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

'''print('=-'*10)
print('    Ímpar ou Par')
print('=-'*10)

numero = input('Digite um número inteiro: ')
if numero.isdigit():
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print(f'O número escolhido "{numero_int}" é par!')
    else:
        print(f'O número escolhido "{numero_int}" é ímpar!')
else:
    print('Você não digitou um número inteiro!')'''


'''Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''

'''entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)
    
    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
    elif hora >=  18 and hora <= 23:
        print('Boa noite')
    else:
        print('Não conheço essa hora.')

except:
    print('Por favor digite apenas números inteiros.')'''



'''Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".'''

nome = input('Digite o seu primeiro nome: ')
letras_nome = len(nome)

if letras_nome > 1:
    if letras_nome <= 4:
        print('nome curto')
    elif letras_nome >= 5 and letras_nome <= 6:
        print('Nome normal')
    else:
        print('nome grande')
else:
    print('Digite mais de uma letra!')
