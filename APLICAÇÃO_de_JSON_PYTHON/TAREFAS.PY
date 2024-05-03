import json

def carregar_tarefas():
    try:
        with open('tarefas.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"tarefas": []}
    
def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as file:
        json.dump(tarefas, file, indent=2)

def adicionar_tarefa(tarefas):
    descricao = input("Digite a descrição da tarefa:")
    nova_tarefa = {
        "descricao": descricao,
        "concluida": False
    }

    tarefas["tarefas"].append(nova_tarefa)
    salvar_tarefas(tarefas)
    print("Tarefas adicionada com sucesso!")

def listar_tarefas(tarefas):
    if not tarefas["tarefas"]:
        print("Não há tarefas cadastradas")
    else:
        for i, tarefa in enumerate(tarefas["tarefas"], start=1):
            status = "concluída" if tarefa["concluida"] else "pendente"
            print(f'{i}. [{status}] {tarefa["descricao"]}')

def marcar_como_concluida(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa que deseja marcar como concluida")) -1
        if 0 <= indice <len(tarefas["tarefas"]):
            tarefas["tarefas"][indice]["concluida"] = True
            salvar_tarefas(tarefas)
            print("tarefa marcada como concluida")
        else:
            print("indice invalido")
    except ValueError:
        print("Digite um numero valido")


def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
        if 0 <= indice < len(tarefas["tarefas"]):
            tarefa_removida = tarefas["tarefas"].pop(indice)
            salvar_tarefas(tarefas)
            print(f'Tarefa "{tarefa_removida["descricao"]}" removida com sucesso.')
        else:
            print("Índice inválido.")
    except ValueError:
        print("Digite um número válido.")




def main():
    tarefas = carregar_tarefas()

    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar como Concluída")
        print("4. Remover Tarefa")
        print("5. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            adicionar_tarefa(tarefas)
        elif opcao == '2':
            listar_tarefas(tarefas)
        elif opcao == '3':
            marcar_como_concluida(tarefas)
        elif opcao == '4':
            remover_tarefa(tarefas)
        elif opcao == '5':
            print('Saindo...')
            break
        else:
            print('Opção inválida')

if __name__ == "__main__":
    main()