# Faça um programa que receba o salário base de um funcionário, 
# calcule e mostre seu a salário a receber,
# sabendo que o funcionário tem gratificação de 5% sobre o salário,
# e paga imposto de 8% tambem sobre o salário base.


sal = salnovo = grat = imp = 0 

sal = int(input('Informe o salário base do funcionário: R$'))

grat = sal * (5/100)
imp = sal * (8/100)
salnovo = (grat + sal) - imp

print('O novo salário do funcionário será: R$',salnovo)