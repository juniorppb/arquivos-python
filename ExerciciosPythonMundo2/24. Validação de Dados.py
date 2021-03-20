sexo = str(input('Informe o seu sexo? [M/F]')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados ínválidos. Por favor, informe seu sexo: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))