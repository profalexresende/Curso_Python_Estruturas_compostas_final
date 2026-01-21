# Aula 02 – Lista de Dicionários

# Cada personagem é um dicionário
# A lista guarda vários personagens
personagens = [
    {"nome": "Arthos", "classe": "Guerreiro", "nivel": 1},
    {"nome": "Luna", "classe": "Maga", "nivel": 2}
]

# Exibindo os personagens
for personagem in personagens:
    print("Nome:", personagem["nome"])
    print("Classe:", personagem["classe"])
    print("Nível:", personagem["nivel"])
    print()
