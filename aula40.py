while True:
    primeiro_num = input('Digite o primeiro número: ')
    segundo_num = input('Digite o segundo número: ')

    numeros_validos = None

    try:
        float_num_1 = float(primeiro_num)
        float_num_2 = float(segundo_num)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operador = input('''Qual operador deseja usar? 
    + : Adição
    - : Subtração
    / : Divisão
    * : Multiplicação
    operador: ''')

    opreadores_permitidos = '+-/*'
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    elif operador not in opreadores_permitidos:
        print('Operador inválido')
    
        continue 
    
    if operador == '+':
        adicão = float_num_1 + float_num_2
        print(f'A soma de {float_num_1} + {float_num_2} é igual a {adicão}')

    elif operador == '-':
        subtracao = float_num_1 - float_num_2
        print(f'A subtraçãoo de {float_num_1} - {float_num_2} é igual a {subtracao}')
    elif operador == '/':
        divisao = float_num_1 / float_num_2
        print(f'A Divisão de {float_num_1} para {float_num_2} é igual a {divisao}')
    elif operador == '*':
        multiplicacao = float_num_1 * float_num_2
        print(f'A multiplicação de {float_num_1} * {float_num_2} é igual a {multiplicacao}')
    else:
        print('Operador inválido, tente novamente!')

    continuar = input('Deseja continuar? [s/n]').lower().startswith('s')
    
    if continuar is False:
        print('Até Logo!')
        break
