from random import randint
computador = randint(0, 11)
print('Sou seu computador... Acabei de pensar em um número de 0 a 10, tente adivinhar!')
acertou = False
palpites = 0
while not acertou:
jogador = int(input('Qual é o seu palpite?'))
palpites += 1
if jogador == computador:
    acertou = True
        else:
            if jogador < computador:
                print('Mais... tente mais uma vez.')
            elif jogador > computador:
                print('Menos... tente mais uma vez.')
    print('Acertou com {} tentativas. PARÁBENS!!'.format(palpites))
