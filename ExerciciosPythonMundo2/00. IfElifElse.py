nome = str(input('Qual o seu nome? '))
if nome == 'Wellyton':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'João':
    print ('Seu nome é bem popular no Brasil.')
elif nome in 'Lígia Janaina Juliana Daniela Claúdia':
    print ('Belo nome feminino.')
else:
    print('Bacana!')
print('Tenha um ótimo dia, {}!'.format(nome))
