# Faça um programa que receba o valor de um depósito, 
# e o valor da taxa de juros,
# calcule e mostre o valor total do rendimento, 
# e o valor total depois do rendimento.

dep = taxa = rend = valortotal = 0 

dep = float(input('Informe o valor do depósito:'))
taxa = float(input('Informe o valor do juros:'))

rend = dep * (taxa/100)
valortotal = dep + rend

print('O valor do rendimento foi de R$', rend)
print('O valor total após o rendimento foi de R$', valortotal)