num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes.'.format(num, tot))
if tot == 2:
    print('Por isso ele É PRIMO.')
else:
    print('Por isso ele NÃO É PRIMO.')
