agenda = {}

def adicionar_contato(agenda):

    nome = input("Digite o nome do contato: ").strip().lower()
    telefone = input("Digite o número do contato: ").strip().lower()

    if telefone in agenda:
        print(f"Este contato já está agendado.") 
    else:
        agenda[nome] = telefone
        print("Contato adicionado com sucesso!")

def buscar_contato(agenda):
    nome = input("Digite o nome do contato: ").strip().lower()

    resultado = agenda.get(nome, "Este contato não está cadastrado na agenda!" )
    print(f"Resultado da busca: {resultado}")

def remover_contato(agenda):
    nome_excluido = input("Digite o nome do contato que deseja excluir: ").strip().lower()

    if nome_excluido in agenda:
        del agenda[nome_excluido]
        print("Exclusão feita com sucesso!")
    else:
        print("Este contato não está cadastrado na agenda!")

def listar_contatos(agenda):
    if len(agenda) == 0:
        print("Não há contatos cadastrados.")
    else: 
        for nome, telefone in agenda.items():
            print(f"Nome: {nome} - Tel: {telefone}")

while True:
    print("----MENU----")
    print("1 - Adicionar Contato")
    print("2 - Buscar Contato")
    print("3 - Remover Contato")
    print("4 - Listar Contatos")
    print("5 - Sair")

    opcao = input("Escolha uma opção (1 - 5): ").strip().lower()

    if (opcao == "1"):
        adicionar_contato(agenda)
    elif (opcao == "2"):
        buscar_contato(agenda)
    elif (opcao == "3"):
        remover_contato(agenda)
    elif (opcao == "4"):
        listar_contatos(agenda)
    elif (opcao == "5"):
        print("Programa encerrado!")
        break
    else:
        print("Opção inválida. Escolha uma das 5 opções (1 - 5)!")

