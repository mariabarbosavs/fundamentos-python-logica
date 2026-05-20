# Faça um programa que receba o salário base de um funcionário, 
# e receba seu percentual de aumento,
# calcule e mostre seu novo salário,
# e o valor do aumento.

sal = salnovo = perc_aum = aum = 0

sal = int(input('informe o salario do funcionario: R$'))
perc_aum = int(input('digite o percentual de aumento desse funcionario:', )) 

aum = sal*(perc_aum/100)
salnovo = sal + aum 

print("o novo salario da funcionario é R$", salnovo)
print("e seu aumento foi de R$", aum)