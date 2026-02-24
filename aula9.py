# Aula 07 – Introdução às Estruturas Compostas

# Lista de personagens (Lista de Dicionários)
personagens = [
    {
        "nome": "Arthos",
        "classe": "Guerreiro",
        "nivel": 1,
        
        # Inventário do personagem (Dicionário com Lista)
        "inventario": [
            ("Espada de Ferro", "arma"),      # Tupla
            ("Poção de Cura", "poção")        # Tupla
        ]
    }
]


# Aula 08 – Criação de Personagens com Estruturas Compostas

# Lista que armazenará todos os personagens
personagens = []

# Função para criar um novo personagem
def criar_personagem():
    nome = input("Nome do personagem: ")
    classe = input("Classe do personagem: ")
    nivel = int(input("Nível do personagem: "))

    personagem = {
        "nome": nome,
        "classe": classe,
        "nivel": nivel,
        # Inventário começa vazio e será usado em aulas futuras
        "inventario": []
    }

    personagens.append(personagem)


# Aula 09 – Inventário do Personagem

# Função para adicionar um item ao inventário de um personagem
def adicionar_item_inventario():
    nome = input("Nome do personagem: ")

    for personagem in personagens:
        if personagem["nome"] == nome:
            item_nome = input("Nome do item: ")
            item_tipo = input("Tipo do item (arma, poção, armadura): ")

            # Cada item é uma tupla
            item = (item_nome, item_tipo)

            # O inventário é uma lista de tuplas
            personagem["inventario"].append(item)

            print("Item adicionado ao inventário!\n")
            return

    print("Personagem não encontrado.\n")
