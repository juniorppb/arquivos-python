soma = 0
cont = 0
for imp in range(1, 501, 2):
    if imp % 3 == 0:
        cont = cont + 1
        soma = soma + imp
print('A soma de todos os {}  valores solicitados é : {} '.format(cont, soma))
