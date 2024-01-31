# Função para solicitar a seleção de colunas
def selecionar_colunas():
    colunas = input("\nDigite as colunas desejadas separadas por vírgula: ")
    return colunas

# Função para solicitar a seleção de tabelas
def selecionar_tabelas():
    tabelas = input("\nDigite as tabelas desejadas separadas por vírgula: ")
    return tabelas

# Função para solicitar as condições da cláusula WHERE
def selecionar_condicoes():
    condicoes = input("\nDigite as condições da cláusula WHERE: ")
    return condicoes

# Função para criar consultas SQL SELECT
def criar_consulta_select():
    colunas = selecionar_colunas()
    tabelas = selecionar_tabelas()
    condicoes = selecionar_condicoes()

    consulta_sql = f"SELECT {colunas} FROM {tabelas}"
    if condicoes:
        consulta_sql += f" WHERE {condicoes}"

    print("\nConsulta SQL SELECT gerada:")
    print(consulta_sql)

# Função para criar comandos SQL UPDATE
def criar_comando_update():
    tabela = input("\nDigite o nome da tabela que deseja atualizar: ")
    colunas_valores = input("\nDigite as colunas e valores a serem atualizados no formato 'coluna1 = valor1, coluna2 = valor2': ")
    condicoes = selecionar_condicoes()

    comando_sql = f"UPDATE {tabela} SET {colunas_valores}"
    if condicoes:
        comando_sql += f" WHERE {condicoes}"

    print("\nComando SQL UPDATE gerado:")
    print(comando_sql)

# Função para criar comandos SQL INSERT
def criar_comando_insert():
    tabela = input("\nDigite o nome da tabela em que deseja inserir os valores: ")
    colunas = input("Digite as colunas em que deseja inserir os valores, separadas por vírgula: ")
    valores = input("Digite os valores que deseja inserir, separados por vírgula: ")

    comando_sql = f"INSERT INTO {tabela} ({colunas}) VALUES ({valores})"

    print("\nComando SQL INSERT gerado:")
    print(comando_sql)

# Função principal
def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Criar Consulta SQL SELECT")
        print("2. Criar Comando SQL UPDATE")
        print("3. Criar Comando SQL INSERT")
        print("4. Sair")
        opcao = input("\nOpção: ")

        if opcao == "1":
            criar_consulta_select()
        elif opcao == "2":
            criar_comando_update()
        elif opcao == "3":
            criar_comando_insert()
        elif opcao == "4":
            print("\nSaindo do Construtor de Consultas SQL.\n")
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()
