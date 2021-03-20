pesomaior = 0
pesomenor = 0
for p in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
print('O maior peso lido foi de {} KG.'.format(pesomaior))
print('E o menor peso foi de {} KG.'.format(pesomenor))