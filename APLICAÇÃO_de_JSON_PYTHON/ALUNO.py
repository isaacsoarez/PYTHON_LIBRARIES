import json

def carregar_dados():
    try:
        with open('aluno.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
def salvar_dados(dados):
    with open('aluno.json', 'w') as file:
        json.dump(dados, file, indent=4)

def adicionar_disciplina(aluno, nome_disciplina):
    if nome_disciplina not in aluno["disciplinas"]:
        aluno["disciplinas"][nome_disciplina] = []
        print(f"Disciplina '{nome_disciplina}' adicionada para o aluno '{aluno['nome']}'")
    else:
        print(f"Disciplina '{nome_disciplina}' já existe para o aluno '{aluno['nome']}'")

def adicionar_nota(aluno, nome_disciplina, nota):
    if nome_disciplina in aluno["disciplinas"]:
        aluno["disciplinas"][nome_disciplina].append(nota)
        print(f"Nota {nota} adicionada para a disciplina '{nome_disciplina}' do aluno '{aluno['nome']}'")
    else:
        print(f"Disciplina '{nome_disciplina}' não encontrada para o aluno '{aluno['nome']}'")

def calcular_media_disciplina(aluno, nome_disciplina):
    if nome_disciplina in aluno["disciplinas"]:
        notas = aluno["disciplinas"][nome_disciplina]
        if notas:
            media = sum(notas) / len(notas)
            print(f"Média na disciplina '{nome_disciplina}' do aluno '{aluno['nome']}': {media:.2f}")
        else:
            print(f"O aluno '{aluno['nome']}' ainda não possui notas na disciplina '{nome_disciplina}'")
    else:
        print(f"Disciplina '{nome_disciplina}' não encontrada para o aluno '{aluno['nome']}'")

def calcular_media_geral(aluno):
    notas_totais = []
    for disciplina, notas in aluno["disciplinas"].items():
        notas_totais.extend(notas)
    if notas_totais:
        media_geral = sum(notas_totais) / len(notas_totais)
        print(f"Média geral do aluno '{aluno['nome']}': {media_geral:.2f}")
    else:
        print(f"O aluno '{aluno['nome']}' ainda não possui notas em nenhuma disciplina")

def menu():
    print("\nMenu de Opções:")
    print("1. Adicionar disciplina")
    print("2. Adicionar nota")
    print("3. Calcular média de disciplina")
    print("4. Calcular média geral")
    print("5. Sair do programa")

def main():
    dados = carregar_dados()
    aluno_nome = input("Digite o nome do aluno: ")
    aluno = dados.get(aluno_nome, {"nome": aluno_nome, "disciplinas": {}})
    
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            disciplina = input("Digite o nome da disciplina a ser adicionada: ")
            adicionar_disciplina(aluno, disciplina)
        elif opcao == "2":
            disciplina = input("Digite o nome da disciplina: ")
            nota = float(input("Digite a nota a ser adicionada: "))
            adicionar_nota(aluno, disciplina, nota)
        elif opcao == "3":
            disciplina = input("Digite o nome da disciplina: ")
            calcular_media_disciplina(aluno, disciplina)
        elif opcao == "4":
            calcular_media_geral(aluno)
        elif opcao == "5":
            salvar_dados(dados)
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
