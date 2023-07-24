# texto = iter('Warley')

# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
 
#iterador -> quem sabe entregar um valor por vez 
#next -> me entregue o próximo valor
#iter -> me entregue seu iterador

# for letra in texto
texto = 'Warley Ferraz Almeida' #iterável
# iterador = iter(texto) #iterator

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break


for letra in texto:
    print(letra)