# Faça um programa que receba o salário base de um funcionário, 
# calcule e mostre seu a salário a receber,
# sabendo que o funcionário tem gratificação de R$50,00,
# e paga imposto de 10% sobre o salário base.

salnovo = sal = imp = 0 

sal = int(input('Informe o salário base do funcionário: R$'))

imp = sal * (10/100)
salnovo = (sal + 50) - imp

print('O novo salário do funcionário é de: R$',salnovo)