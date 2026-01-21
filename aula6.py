# Aula 06 – Estrutura completa do personagem

personagens = [
    {
        "nome": "Arthos",
        "classe": "Guerreiro",
        "nivel": 1,
        "inventario": [
            ("Espada", "arma"),
            ("Poção", "poção")
        ]
    }
]

# Exibindo tudo
for personagem in personagens:
    print("Nome:", personagem["nome"])
    print("Classe:", personagem["classe"])
    print("Nível:", personagem["nivel"])
    print("Inventário:")

    for item in personagem["inventario"]:
        print("-", item[0], "(" + item[1] + ")")

    print()
