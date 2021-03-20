from time import sleep
um = int(input('Primeiro valor: '))
dois = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplcar
    [ 3 ] maior 
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>> Qual sua opção? '))
    if opcao == 1:
        soma = um + dois
        print('A soma entre {} + {} é igual {}.'.format(um, dois, soma))
    elif opcao == 2:
        mult = um * dois
        print('A resultado de {} x {} é igual {}.'.format(um, dois, mult))
    elif opcao == 3:
        if um > dois:
            maior = um
        else:
            maior = dois
            print('Entre {} e {}, o maior é {}.'.format(um, dois, maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        um = int(input('Primeiro valor: '))
        dois = int(input('Segundo valor: '))
    elif opcao == 5:
        print('FINALIZANDO...')
    else:
        print('Opção Inválida! Tente novamente.')
    print('=-='*15)
    sleep(2)
print('Fim do programa. Volte sempre!')
