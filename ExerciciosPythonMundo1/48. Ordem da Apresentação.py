import random
a1 = str(input('Qual o nome do primeiro aluno?'))
a2 = str(input('QUal o nome do segundo aluno?'))
a3 = str(input('Qual o nome do terceiro aluno?'))
a4 = str(input('Qual o nome do quarto aluno?'))
nomes = [a1, a2, a3, a4]
ordem = random.shuffle(nomes)
print('Qual a ordem para a apresentação do trabalho')
print(nomes)