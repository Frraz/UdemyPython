# senha_salva = '123456'
# senha_digitada = ''
# repetições = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repetições}x): ')

#     repetições += 1
# print(repetições)
# print('Aquele laço acima pode ter repetição infinitas.')

texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')