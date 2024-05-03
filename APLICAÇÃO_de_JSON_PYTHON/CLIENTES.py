import json 

def carregar_clientes():
    with open('clientes.json', 'r') as file:
        return json.load(file)
    
def salvar_clientes(clientes):
    with open('clientes.json', 'w') as file:
        json.dump(clientes, file, indent=2)

def adicionar_clientes(clientes):
    id_cliente = int(input("Digite o id do cliente:"))
    nome = (input("Digite deu nome:"))
    idade = int(input("Digite sua idade:"))
    email = (input("Digite seu email:"))
    telefone = (input("Digite seu telefone:"))
    
    novo_cliente = {
    "id" : id_cliente,
    "nome" : nome,
    "idade" : idade,
    "email" : email,
    "telefone": telefone    
    }
    
    clientes["clientes"].append(novo_cliente)
    salvar_clientes(clientes)
    print('Cliente adicionado com sucesso')

def listar_clientes(clientes):
    for cliente in clientes["clientes"]:
        print(f"ID: {cliente['id']}, Nome: {cliente['nome']}, Idade: {cliente['idade']}, Email: {cliente['email']}, Telefone: {cliente['telefone']}")

def main():
    clientes = carregar_clientes() 

    while True:
        print("\n1. Adicionar Cliente")
        print("2. Listar Clientes")
        print("3. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            adicionar_clientes(clientes)
        elif opcao == '2':
            listar_clientes(clientes)
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":

    main()