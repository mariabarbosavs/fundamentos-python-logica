class Usuario:
    def __init__(self, id_usuario, nome):
        self.__id_usuario = id_usuario
        self.__nome = nome

    def get_nome(self):
        return self.__nome
    
    def get_id_usuario(self):
        return self.__id_usuario        

class Tarefa:
    def __init__(self, id_tarefa, titulo, usuario_responsavel):
        self.__id_tarefa = id_tarefa
        self.__titulo = titulo
        self.__usuario_responsavel = usuario_responsavel
        self.__status = "Pendente"

    def get_nome_responsavel(self):
        return self.__usuario_responsavel.get_nome()

    def get_titulo(self):
        return self.__titulo

    def get_status(self):
        return self.__status
    
    def concluir_tarefa(self):
        self.__status = "Concluida"

class Gerenciador:
    def __init__(self):
        self.__lista_tarefas = []

    def adicionar_tarefa(self, nova_tarefa):
        self.__lista_tarefas.append(nova_tarefa)
        print("Tarefa adicionada com sucesso!")

    def listar_tarefas(self):
        if len(self.__lista_tarefas) == 0:
            print("Não há nenhuma tarefa cadastrada.")
        else:
            for i, tarefa_obj in enumerate(self.__lista_tarefas, start=1):
                titulo = tarefa_obj.get_titulo()
                status = tarefa_obj.get_status()
                responsavel = tarefa_obj.get_nome_responsavel()

                print(f"{i} - {titulo} [{status}] (Responsavel: {responsavel})")

    def remover_tarefa(self, numero):
        if len(self.__lista_tarefas) == 0:
            print("Não há tarefas cadastradas na lista.")
        elif 1 <= numero <= len(self.__lista_tarefas):
            del self.__lista_tarefas [numero - 1]
            print("Tarefa removida com sucesso!")
        else:
            print("Número de tarefa inválido!")
    

def menu():
    meu_gerenciador = Gerenciador()

    print("Bem-Vindo ao Sistema de Gerenciamento de Tarefas Orientado a objetos!")
    nome_usuario = input("Digite seu nome para entrar no sistema: ")

    usuario_atual = Usuario(id_usuario = 1, nome = nome_usuario)
    contado_id_tarefa = 1

    while True:
        print(f"\n---MENU---(Usuário: {usuario_atual.get_nome()})---")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Remover tarefa")
        print("4 - Concluir tarefa")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if (opcao == "1"):
            titulo = input("Adicione uma nova tarefa: ")

            nova_tarefa = Tarefa(id_tarefa=contado_id_tarefa, titulo=titulo, usuario_responsavel=usuario_atual)

            meu_gerenciador.adicionar_tarefa(nova_tarefa)
            contado_id_tarefa += 1

        elif (opcao == "2"):
            meu_gerenciador.listar_tarefas()

        elif (opcao == "3"):
            meu_gerenciador.listar_tarefas()

            try:
                numero = int(input("Digite o índice da tarefa que deseja remover: "))
                meu_gerenciador.remover_tarefa(numero)
            except ValueError:
                print("Por favor digite um índice válido.")

        elif (opcao == "4"):
            meu_gerenciador.listar_tarefas()

            tarefa_concluida = int(input("Digite o índice da tarefa que deseja concluir: "))

            if tarefa_concluida in lista_tarefas.items():
                Tarefa.concluir_tarefa(tarefa_concluida)
                print("Tarefa concluida com sucesso!")
            else:
                print("Tarefa não encontrada.")
            
        elif (opcao == "5"):
            print("Programa encerrado. Até a próxima!")
            break

        else:
            print("Opção inválida.")

menu()
        
        






