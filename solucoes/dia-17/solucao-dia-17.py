import csv

# Inicializa um dicionário vazio para armazenar as despesas
despesas = {}

# Função para carregar as despesas do arquivo CSV
def carregar_despesas():
    try:
        with open("despesas.csv", newline="") as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            for linha in leitor_csv:
                categoria = linha["Categoria"]
                if categoria not in despesas:
                    despesas[categoria] = []
                despesas[categoria].append({
                    "Valor": float(linha["Valor"]),
                    "Descrição": linha["Descrição"],
                    "Data": linha["Data"]
                })
    except FileNotFoundError:
        pass

# Função para salvar as despesas no arquivo CSV
def salvar_despesas():
    with open("despesas.csv", mode="w", newline="") as arquivo_csv:
        nomes_colunas = ["Categoria", "Valor", "Descrição", "Data"]
        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=nomes_colunas)
        escritor_csv.writeheader()
        for categoria, lista_despesas in despesas.items():
            for despesa in lista_despesas:
                escritor_csv.writerow({
                    "Categoria": categoria,
                    "Valor": despesa["Valor"],
                    "Descrição": despesa["Descrição"],
                    "Data": despesa["Data"]
                })

# Carrega as despesas existentes do arquivo CSV
carregar_despesas()

while True:
    print("\n### Calculadora de Despesas Pessoais ###")
    print("1. Registrar nova despesa")
    print("2. Visualizar resumo por categoria")
    print("3. Visualizar resumo por data")
    print("4. Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == '1':
        valor = float(input("\nDigite o valor da despesa: ").replace(",", "."))
        descricao = input("Digite a descrição da despesa: ")
        categoria = input("Digite a categoria da despesa: ")
        data = input("Digite a data da despesa (DD/MM/AAAA): ")

        if categoria not in despesas:
            despesas[categoria] = []
        despesas[categoria].append({
            "Valor": valor,
            "Descrição": descricao,
            "Data": data
        })

        salvar_despesas()
        print("\nDespesa registrada com sucesso!")

    elif opcao == '2':
        print("\nLista de Despesas Por Categoria:")
        for categoria, lista_despesas in despesas.items():
            total_categoria = 0
            for despesa in lista_despesas:
                total_categoria += despesa["Valor"]
            print(f"{categoria}: R${total_categoria:.2f}".replace('.', ','))


    elif opcao == '3':
        data = input("\nDigite a data (DD/MM/AAAA): ")
        total_data = 0
        for lista_despesas in despesas.values():
            for despesa in lista_despesas:
                if despesa["Data"] == data:
                    total_data += despesa["Valor"]
        print(f"Total na data {data}: R${total_data:.2f}".replace('.', ','))


    elif opcao == '4':
        print("\nObrigado por usar a Calculadora de Despesas Pessoais!\n")
        break

    else:
        print("\nOpção inválida. Tente novamente.\n")
