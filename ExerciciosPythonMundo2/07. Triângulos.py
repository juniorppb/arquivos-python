a = float(input('Digite um valor: '))
b = float(input('Digite outro valor: '))
c = float(input('Digite mais um valor: '))
if a == b or b == c:
    print('Com os números digitados, formam um triângulo EQUILATERO.')
elif a <> b and b <> c and c == a and b == c:
    print('Com os números digitados, formam um triângulo ISOSELES.')
else:
    print('Com os número digitados, formam triângulo ESCALENO.')