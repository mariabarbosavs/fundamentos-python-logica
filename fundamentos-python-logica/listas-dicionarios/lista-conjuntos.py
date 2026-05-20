 # lista representa uma sequencia de valores
# sintaxe: nome_lista = [valores]
"""convertendo uma lista (números desordenados e repetidos) para um conjunto-set (remove duplicatas)"""

numeros = [22, 9, 9, 10, 16, 14, 11, 22]

for numero in numeros:
    print(numero)

numeros_unicos = (list(set(numeros)))

print(numeros_unicos)

"""Transformando uma lista em ordenada"""

numeros_list_2 = [5, 10, 3, 5]
numeros_list_2.sort()

print(numeros_list_2)

"""" Usando 'List Comprehension' com 'if' para pegar apenas números maiores que 10"""
maiores_que_10 = [numero for numero in numeros_unicos if numero > 10]
print(maiores_que_10)

"""Buscando valores numa lista"""

busca = 33

if busca in numeros_unicos:
    print(f"Resultado da Busca: O número {busca} foi encontrado na lista")
else: 
    print(f"Resultado da Busca: Não há o número {busca} na lista")


"""Exercicios de fixação Lista, Filtro e Ordenação"""

notas_alunos = [5.5, 9.0, 7.5, 4.0, 8.5, 6.0]

notas_alunos.append(10.0)
notas_alunos.sort()

aprovados = [nota for nota in notas_alunos if nota >= 7 ]

print(f"As notas aprovadas são {aprovados}")

"""Exercicios de fixação Tuplas, Dicionários, Busca e Agrupamento"""

catalogo = {
    "Eletrônicos": ("Celular", "Notebook"),
    "Roupas": ("Calça", "Vestido"),
}

if "Eletrônicos" in catalogo:
    print(f"Produtos encontrados na seção de Eletrônicos: {catalogo['Eletrônicos']}")