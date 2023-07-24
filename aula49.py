lista = [10, 20, 30, 40]
#lista[2] = 300
#del lista[2]
lista.append(50) #Adicionar um item no final da lista.
lista.pop() #Remove o último item da lista.
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido', ultimo_valor)
