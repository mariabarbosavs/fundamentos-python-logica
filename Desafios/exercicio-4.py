# Faça um programa que receba o salário base de um funcionário, 
# calcule e mostre seu novo salário,
# sabendo que o mesmo recebeu um aumento de 50%.


sal = salnovo = aum = 0 

sal = float(input("digite o salario do funcionario:" ))

aum = sal *(50/100)
salnovo = sal + aum

print("o salario do funcionario apos o aumento de 50% é R$", salnovo)