n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
if n1 > n2:
    print('{} é o maior número.'.format(n1))
elif n1 < n2:
    print ('{} é o maior número.'.format(n2))
elif n1 == n2:
    print ('O número {} é igual ao número {}.'.format(n1,n2))