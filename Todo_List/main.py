import json
import os

# Declarações das variáveis
dados = {}

# Verificar se o arquivo JSON existe e não está vazio
if os.path.isfile('dados.json') and os.path.getsize('dados.json') > 0:
    # Carregar os dados existentes do JSON
    with open('dados.json') as arquivo:
        dados = json.load(arquivo)


# Funções
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    limpar_terminal()
    uso = 0
    while uso != '4':
        print("=-" * 30)
        print("Seja bem-vindo à sua lista de tarefas!")
        print("Por favor, digite qual opção você deseja:")
        print("1 - Cadastrar nova tarefa.")
        print("2 - Ver tarefas cadastradas.")
        print("3 - Editar tarefa.")
        print("4 - Excluir tarefa.")
        print("5 - Sair.")
        uso = input("Digite aqui sua opção: ")
        print("=-" * 30)
        limpar_terminal()

        if uso == '1':
            # Chama a função para cadastrar novas tarefas
            cadastrar_tarefa()
        elif uso == '2':
            # Chama a função para listar as tarefas
            listar_tarefas()
        elif uso == '3':
            modificar_tarefa()
        elif uso == '4':
            excluir_tarefa()
        else:
            print("digite uma opção valida")


def cadastrar_tarefa():
    # Obter os dados da nova tarefa do usuário
    titulo = input("Digite o título da tarefa: ")
    tipo = input("Digite o tipo da tarefa: ")
    andamento = input("Digite o andamento da tarefa - concluída, em andamento: ")

    # Obter o ID da última tarefa cadastrada e incrementá-lo em 1
    ids_numericos = [int(id) for id in dados.keys() if id.isdigit()]
    id = max(ids_numericos, default=0) + 1

    # Criar um dicionário com os dados da nova tarefa
    nova_tarefa = {
        "id": id,
        "titulo": titulo,
        "tipo": tipo,
        "andamento": andamento
    }

    # Adicionar a nova tarefa ao dicionário de tarefas existentes
    dados[str(id)] = nova_tarefa

    # Salvar os dados atualizados de volta no JSON
    with open('dados.json', 'w') as arquivo:
        json.dump(dados, arquivo)

    print("Tarefa adicionada com sucesso!")
    limpar_terminal()


def listar_tarefas():
    limpar_terminal()
    print("=-" * 30)
    print("Listagem de tarefas")
    if not dados:
        print("Nenhuma tarefa cadastrada.")
    else:
        for id, tarefa in dados.items():
            print("-" * 30)
            print("Título:", tarefa.get("titulo", ""))
            print("Tipo:", tarefa.get("tipo", ""))
            print("Andamento:", tarefa.get("andamento", ""))
            print("-" * 30)



def modificar_tarefa():
    limpar_terminal()
    print("=-" * 30)
    print("Modificação de tarefas")
    id_tarefa = input("Digite o ID da tarefa que deseja modificar: ")

    tarefa = dados.get(id_tarefa)
    if tarefa:
        print("=-" * 30)
        print("Tarefa encontrada:")
        print("ID:", tarefa.get("id"))
        print("Título:", tarefa.get("titulo"))
        print("Tipo:", tarefa.get("tipo"))
        print("Andamento:", tarefa.get("andamento"))

        print("=-" * 30)
        print("1 - Mudar nome.")
        print("2 - Mudar tipo.")
        print("3 - Mudar andamento.")
        opcao = input("Digite a opção desejada: ")
        print("=-" * 30)

        if opcao == '1':
            novo_nome = input("Digite o novo nome: ")
            tarefa['titulo'] = novo_nome
            print("Nome da tarefa modificado com sucesso!")
            print("=-" * 30)
        elif opcao == '2':
            novo_tipo = input("Digite o novo tipo: ")
            tarefa['tipo'] = novo_tipo
            print("Tipo da tarefa modificado com sucesso!")
            print("=-" * 30)
        elif opcao == '3':
            novo_andamento = input("Digite o novo andamento: ")
            tarefa['andamento'] = novo_andamento
            print("Andamento da tarefa modificado com sucesso!")
            print("=-" * 30)
        else:
            print("Opção inválida.")
            print("=-" * 30)
    else:
        print("Tarefa não encontrada.")

def excluir_tarefa():
    limpar_terminal()
    print("=-" * 30)
    print("Exclusão de tarefa")
    id_tarefa = input("Digite o ID da tarefa que deseja excluir: ")

    tarefa = dados.get(id_tarefa)
    if tarefa:
        confirmacao = input("Tem certeza que deseja excluir a tarefa? (s/n): ")
        if confirmacao.lower() == 's':
            del dados[id_tarefa]
            print("Tarefa excluída com sucesso!")
        else:
            print("Exclusão da tarefa cancelada.")
    else:
        print("Tarefa não encontrada.")

    limpar_terminal()


main()

print("Volte sempre! Obrigado por usar nosso programa.")
