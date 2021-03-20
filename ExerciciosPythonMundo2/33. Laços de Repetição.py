#cont = 1
#while cont <= 10:
 #   print(cont, '-> ', end='')
  #  cont += 1
#print('Acabou') ''' está correto

#n = s = 0
#while n != 999:
 #   n = int(input('Digite um número: '))
  #  s += n
#print('A soma vale {}.'.format(s)) ''' está correto

#nome = José
#idade = 33
#salario = 987.3
#print(f'O {nome:^20} tem {idade} anos e ganha R$ {salario:.2f}.') utilizando fStrings



n = s = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}.'.format(s)) ''' abaixo f string
print(f'A soma vale {s}.')
