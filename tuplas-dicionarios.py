"""Agrupando dados com dicionários e tuplas"""

equipe = {
    "Alunos": ('Maria', 'Vinicius'),
    "Professores": ('Helena', 'Cecilia'),
}

"""Buscando e imprimindo dados do dicionário"""

print(f"As professoras da equipe são {equipe['Professores']}")

"""Exercicios de fixação Tuplas, Dicionários, Busca e Agrupamento"""

catalogo = {
    "Eletrônicos": ("Celular", "Notebook"),
    "Roupas": ("Calça", "Vestido"),
}

if "Eletrônicos" in catalogo:
    print(f"Produtos encontrados na seção de Eletrônicos: {catalogo['Eletrônicos']}")