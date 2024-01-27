import csv

class CalculadoraDespesas:
    def __init__(self):
        self.despesas = {}
        self.carregar_despesas()

    def carregar_despesas(self):
        try:
            with open("despesas.csv", newline="") as arquivo_csv:
                leitor_csv = csv.DictReader(arquivo_csv)
                for linha in leitor_csv:
                    categoria = linha["Categoria"]
                    if categoria not in self.despesas:
                        self.despesas[categoria] = []
                    self.despesas[categoria].append({
                        "Valor": float(linha["Valor"].replace(",", ".")), # Substituir vírgula por ponto
                        "Descrição": linha["Descrição"],
                        "Data": linha["Data"]
                    })
        except FileNotFoundError:
            pass

    def salvar_despesas(self):
        with open("despesas.csv", mode="w", newline="") as arquivo_csv:
            nomes_colunas = ["Categoria", "Valor", "Descrição", "Data"]
            escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=nomes_colunas)
            escritor_csv.writeheader()
            for categoria, lista_despesas in self.despesas.items():
                for despesa in lista_despesas:
                    escritor_csv.writerow({
                        "Categoria": categoria,
                        "Valor": despesa["Valor"],
                        "Descrição": despesa["Descrição"],
                        "Data": despesa["Data"]
                    })

    def registrar_despesa(self, valor, descricao, categoria, data):
        if categoria not in self.despesas:
            self.despesas[categoria] = []
        self.despesas[categoria].append({
            "Valor": valor,
            "Descrição": descricao,
            "Data": data
        })
        self.salvar_despesas()
        print("\nDespesa registrada com sucesso!")

    def resumo_por_categoria(self):
        print("\nLista de Despesas Por Categoria:")
        for categoria, lista_despesas in self.despesas.items():
            total_categoria = sum(despesa["Valor"] for despesa in lista_despesas)
            print(f"{categoria}: R${total_categoria:.2f}".replace('.', ','))

    def resumo_por_data(self, data):
        total_data = sum(despesa["Valor"] for lista_despesas in self.despesas.values() for despesa in lista_despesas if despesa["Data"] == data)
        print(f"Total na data {data}: R${total_data:.2f}".replace('.', ','))

    def menu_principal(self):
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
                self.registrar_despesa(valor, descricao, categoria, data)

            elif opcao == '2':
                self.resumo_por_categoria()

            elif opcao == '3':
                data = input("\nDigite a data (DD/MM/AAAA): ")
                self.resumo_por_data(data)

            elif opcao == '4':
                print("\nObrigado por usar a Calculadora de Despesas Pessoais!\n")
                break

            else:
                print("\nOpção inválida. Tente novamente.\n")

if __name__ == "__main__":
    calculadora = CalculadoraDespesas()
    calculadora.menu_principal()
