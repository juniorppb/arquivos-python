produto = float(input('Qual o valor do produto: R$ '))
dez = produto * 10 / 100
cinco = produto * 5 / 100
vinte = produto * 20 / 100
print('O produto que você deseja comprar custa R$ {:.2f}.'.format(produto))
print('''Temos as seguintes opções de pagamentos: 
[ 1 ] À vista.
[ 2 ] À vista no cartão.
[ 3 ] Parcelado em 2 vezes.
[ 4 ] Parcelamento em mais vezes''')
opção = int(input('Qual forma de pagamento você prefere? '))
if opção == 1:
    print('À vista (dinheiro ou cheque), você recebe um desconto de R$ {:.2f}, por isso, pagará o valor de R$ {:.2f}.'.format(dez, produto - dez))
elif opção == 2:
    print('À vista no cartão, você recebe um desconto de R$ {:.2f}, por isso, pagará o valor de R$ {:.2f}.'.format(cinco, produto - cinco))
elif opção == 3:
    print('O seu produto foi parcelado, o valor ficou em, 2 x de R$ {:.2f}.'.format(produto / 2))
elif opção == 4:
    parcela = int(input('Quantas vezes você quer parcelar?'))
    print('O seu produto foi parcelado, o valor ficou em, {} x de R$ {:.2f}.'.format(parcela, (vinte + produto) / parcela))