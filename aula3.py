# Aula 03 – Criar personagens com função

personagens = []

def criar_personagem():
    nome = input("Nome do personagem: ")
    classe = input("Classe do personagem: ")
    nivel = int(input("Nível do personagem: "))

    personagem = {
        "nome": nome,
        "classe": classe,
        "nivel": nivel
    }

    personagens.append(personagem)

    print ("---Dados do personagem criado---")
    print("Nome:", personagem["nome"])
    print("Classe:", personagem["classe"])
    print("Nível:", personagem["nivel"])

criar_personagem()