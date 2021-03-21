lanche = ('Hamburguer','Churrasco','Pizza','Pudim','Batata Frita')
print(lanche)
print('-'*20)
print(sorted(lanche))
print('-'*20)
print(f'Eu comi {lanche[1]}')
print('-'*20)
for comida in lanche:
    print(f'Eu vou comer {comida}.')
print('Comi pra caramba.')
print('-'*20)
for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi pra caramba!')
print('-'*20)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')
print('-'*20)

