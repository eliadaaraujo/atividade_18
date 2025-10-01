# Crie um dicionário chamado notas com as chaves: Matemática, Português, História. Atribua valores (notas) e exiba a média.
notas = {
    "Matemática": 10.0,
    "Português": 8.0,
    "História": 7.5,
}

media = sum(notas.values()) / 3

print("Média:", media)