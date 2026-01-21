# Aula 01 – Introdução às Estruturas Compostas

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


# Aula 02 – Criação de Personagens com Estruturas Compostas

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
