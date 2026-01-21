# Aula 04 – Dicionário com lista interna

personagem = {
    "nome": "Arthos",
    "classe": "Guerreiro",
    "nivel": 1,
    "inventario": []  # Lista dentro do dicionário
}

# Adicionando itens ao inventário
personagem["inventario"].append("Espada")
personagem["inventario"].append("Poção")

print(personagem)
