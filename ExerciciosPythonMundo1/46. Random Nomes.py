import random
aluno1 = str(input('Qual o nome do primeiro aluno?'))
aluno2 = str(input('QUal o nome do segundo aluno?'))
aluno3 = str(input('Qual o nome do terceiro aluno?'))
aluno4 = str(input('Qual o nome do quarto aluno?'))
nomes = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(nomes)
print('O escolhido foi {}.'.format(escolhido))