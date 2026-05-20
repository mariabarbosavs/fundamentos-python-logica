boletim = {
    "Carlos": [7.0, 8.5],
    "Julia": [9.0, 9.5, 10.0],
    "Pedro": [5.0]
}

boletim ["Pedro"].append(7.5)

medias_finais = []

for nome, nota in boletim.items():
    media_final = sum(nota)/len(nota)

    medias_finais.append((nome, media_final))
    print(f"Média calculada para: {nome} - {media_final}")

print(f"\nLista de Médias Finais: {medias_finais}")

