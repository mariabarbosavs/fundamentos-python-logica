vendas_do_dia = [
    ("Cecilia", "Mexerica"), ("Vinicius", "Maçã"),
    ("Vinicius", "Uva"), ("Maria", "Uva"), 
    ("Maria Claudia", "Uva")
]

frutas = set()
for cliente, fruta in vendas_do_dia:
    frutas.add(fruta)

print(f"Essas são as frutas vendidas no dia: {frutas}")

