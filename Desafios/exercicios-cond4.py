# Faça um programa que receba o codigo correspondente a um cargo de um funcionário e seu salario atual,
# mostre o cargo,
# o valor do aumento, 
# e seu novo salario. 

# Tabela; cod   cargo       percentual
#          1  escrituario    50%
#          2  secretario     35%
#          3   caixa         20%
#          4   gerente       10%
#          5   diretor        0%

cargos = {
    1: ("Escrituário", 0.50),
    2: ("Secretário", 0.35),
    3: ("Caixa", 0.20),
    4: ("Gerente", 0.10),
    5: ("Diretor", 0.00)
}

cod = 0
sal = 0
aum = 0 
salnovo = 0  
mod = 0

cod = int(input('Digite o código do funcionário (1 a 5): '))
sal = float(input('Digite o salário desse mesmo funcionário: R$'))

if cod in cargos:
    cargo, percentual = cargos[cod]
    aum = sal * percentual
    salnovo = sal + aum

    print("\n--- Resultado ---")
    print(f"Cargo: {cargo}")
    print(f"Aumento: R$ {aum:.2f}")
    print(f"Novo salário: R$ {salnovo:.2f}")
else:
    print("Código inválido! Tente novamente.")