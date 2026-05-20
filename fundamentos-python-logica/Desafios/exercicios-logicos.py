# Dada as variaveis numericas x, y e z
# contendo os valores 2, 5 e 9 respectivamente,
# a variavel literal NOME contendo o literal MARIA,
# e a variavel logica SIM contendo o valor logico FALSO,
# observe os resultados obtidos das expressões logicas a seguir:

x = 2
y = 5
z = 9
a = 1
b = 10

NOME = 'Maria'
SIM = False

print("os valores das variaveis x e y são maiores que z? E NOME = Maria?", z < x + y and NOME == 'Maria', '\n')

print("SIM or y >= x", SIM or y >= x, '\n')

print('NOME = Jorge? and SIM or x < z + b?', NOME == 'Jorge' and SIM or x < z + b, '\n')

print('not SIM or quociente-z,y + a = x?', not SIM or (z/y + a == x ))