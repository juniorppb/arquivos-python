n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Sua nota média é de {:.2f}. Você foi REPROVADO!.'.format(media))
elif media >= 5 or media <= 7:
    print('Sua nota média é de {}. Você ficou em RECUPERAÇÂO.'.format(media))
else:
    print('Sua nota média é de {}. PARABÉNS! VOCÊ FOI APROVADO.'.format(media))