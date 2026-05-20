# Faça um programa que receba dois números e mostre o maior.

n1 = n2 = 0

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if (n1 > n2): 
    print(n1, 'é maior que', n2)
else: 
    print(n2, 'é maior que', n1)
