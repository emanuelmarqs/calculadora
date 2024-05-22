#Criar calculadora

while True:  #é como se fosse o do while

    #declaração de variáveis
    n1 = str(input("Digite o primeiro número:")).replace(',','.')
    n1 = float(n1)

    print('Informe a operação que você deseja: \n')
    print('"+" para SOMA')
    print('"-" para SUBTRAÇÃO')
    print('"*" para MULTIPLICAÇÃO')
    print('"/" para DIVISÃO')
    print('"%" para encontrar o resto da DIVISÃO')

    op = input('Operação desejada.')

    n2 = str(input("Digite o segundo número:")).replace(',','.')

    n2 = float(n2)

    match op: 
        case '+':
            print(f'A soma é {n1+n2}.')
        case '-':
            print(f'A subtração é {n1-n2}')
        case '*':
            print(f'A multiplicação é {n1*n2}')
        case '/':
            print(f'A divisão é {n1/n2}')
        case _:
            print('Operação Inválida!')
            continue        #continua o loop do zero em um novo loop
    
    #pergunta se o usuário quer continuar ou não

    continuar = input('Deseja continuar (s/n)?')

    #verifica a opção do usuário
    if continuar == 's':
        continue #volta para o inicio do próximo loop
    elif continuar == 'n':
        break #para o programa definitivamente
    else:
        print('Opção inválida')
