# sintaxe 
# print(objetos, argumentos)

nome = 'Maria'
print("Olá " + nome + "! bem vinda") 

print('imprime uma msg e pula de linha')
print('imprime uma msg e permanece na linha', end=" ")
print('- continuo na mesma linha')

nome = 'Maria'
idade = 18

msg_formatada = 'o nome dela é {0} e ela tem {1} anos'.format(nome,idade)
print(msg_formatada)

nome = 'Maria'
peso = 57.0

msg = f'Olá, meu nome é {nome} e eu peso {peso} kg.'
print(msg)  
#      ou
print(f'Olá, meu nome é {nome} e eu peso {peso} kg.') 

a = 10
b = 5

print(f'a soma de {a} com {b} é igual a {a + b}')

valor = 125.586496
print(f'o valor é {valor:.2f}')