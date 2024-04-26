import json

def carregar_contatos():
    try:
        with open('contato.json', 'r') as arquivo:
            contatos = json.load(arquivo)
    except FileNotFoundError:
        contatos = []
    return contatos
                
def salvar_contatos(contatos):
    with open('contatos.json', 'w') as arquivo:
        json.dump(contatos, arquivo) 

def adicionar_contato():
    nome = input("Digite o nome do contato:")
    telefone = input("Digite o telefone do contato:")
    email = input('Digite o email do contato:')

    novo_contato = {"nome" : nome, "telefone" : telefone, "email" : email}
    contatos.append(novo_contato)
    salvar_contatos(contatos)
    print("contato adicionado com sucesso")

def listar_contatos():
    if not contatos:
        print("sem contatos cadstrados")
    else:
        print("lista de contatos:")
        for i, contato in enumerate(contatos, 1):
            print(f"{i}. Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email:{contato['email']}")

def buscar_contato():
    nome_busca = input("Digite o nome do contato que deseja buscar:")
    encontrados = [contato for contato in contatos if contato['nome'].lower() == nome_busca.lower()]
    if encontrados:
        print('contato encontrado:')
        for contato in encontrados:
                        print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email:{contato['email']}")
    else:
         print('contato não encontrado')

contatos = carregar_contatos()

while True:
    print("\n=== Gerenciador de Contatos ===")
    print("1. Adicionar Contatos")
    print("2. Listar Contatos")
    print("3. Buscar Contatos")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        adicionar_contato()
    elif opcao == '2':
        listar_contatos()
    elif opcao == '3':
        buscar_contato()
    elif opcao == '4':
        print("Saindo...")
        break
    else:
        print('Opção inválida')
