nome = str(input('Digite seu nome completo: ')).strip().upper()
print('A letra A aparece {} vezes na frase.'.format(nome.count('A')))
print('A letra A aparece a primeira vez na posição {}.'.format(nome.find('A')+1))
print('A letra A aparece a úlitma vez na posição {}.'.format(nome.rfind('A')+1))
