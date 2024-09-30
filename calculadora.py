validar = True
while validar:
    #primeiro número
    numero_1 = input('Digite o primeiro número: ')
    numero_1 = float(numero_1)

    #operadores
    operador = input('Digite um operador + - * /: ')

    #segundo número
    numero_2 = input('Digite o Segundo número: ')
    numero_2 = float(numero_2)

    #Fezendo o cálculo
    if operador == '+':
        resultado = numero_1 + numero_2

    if operador == '-':
        resultado = numero_1 - numero_2

    if operador == '*':
        resultado = numero_1 * numero_2

    if operador == '/':
        resultado = numero_1 / numero_2

    #mostrar o resultado
    print('Resulado = ', resultado)

    #perguntar se deseja continuar
    conti = input('Deseja fazer outro cálculo: N/S ')

    if conti == 'n' or conti == 'N':
        validar = False

    elif conti == 's' or conti == 'S':
        validar = True

    else:
        print('Você digitou algo ERRADO. reinici novamente:')
        break
