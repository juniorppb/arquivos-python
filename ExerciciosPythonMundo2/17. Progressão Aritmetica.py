print('='*30)
print('10 TERMOS DE UMA P.A.')
print('='*30)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro +(20 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c),end='-')
print('ACABOU!')