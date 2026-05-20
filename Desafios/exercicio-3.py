# Faça um programa que recebe 3 notas,
# e seus respectivos pesos,
# calcule e mostre a média ponderada.

N1 = N2 = N3 = P1 = P2 = P3 = MEDIA = 0

N1 = int(input('digite a 1ª nota:'))
N2 = int(input('digite a 2ª nota:'))
N3 = int(input('digite a 3ª nota:'))
P1 = int(input('digite o peso da  1ª nota:'))
P2 = int(input('digite o peso da  2ª nota:'))
P3 = int(input('digite o peso da  3ª nota:'))

MEDIA = (N1*P1) + (N2*P2) + (N3*P3)/(P1+P2+P3)

print('a media desse aluno é', MEDIA)