um = int(input('Primeiro valor: '))
dois = int(input('Segundo valor: '))
print('''
    [ 1 ] somar
    [ 2 ] multiplcar
    [ 3 ] maior 
    [ 4 ] novos números
    [ 5 ] sair do programa''')
opcao = int(input('>>> Qual sua opção? '))
while opcao == 1:
    soma = um + dois
    print ('A soma dos números é igual a {}.'.format(soma))
        if opcao == 2:
           mult = um * dois
           print('A multiplicação dos números é igual a {}.'.format(mult))
        else:
            if um > dois:
              print('O número {} é maior que {}.'.format(um, dois))
            else:
              print('O número {} é maior que {}.'.format(dois, um))
print('ok')