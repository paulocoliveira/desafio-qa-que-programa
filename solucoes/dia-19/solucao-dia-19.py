# Criação da lista de contatos
contatos = []

# Função para adicionar um novo contato à lista
def adicionar_contato(nome, telefone, email):
    contato = {
        "Nome": nome,
        "Telefone": telefone,
        "E-mail": email
    }
    contatos.append(contato)
    print("\nContato adicionado com sucesso!\n")

# Função para listar todos os contatos
def listar_contatos():
    if not contatos:
        print("\nA agenda está vazia.\n")
    else:
        print("\nLista de Contatos:")
        print("-" * 20)
        for contato in contatos:
            print(f"Nome: {contato['Nome']}")
            print(f"Telefone: {contato['Telefone']}")
            print(f"E-mail: {contato['E-mail']}")
            print("-" * 20)
        print("\n")

# Função para buscar um contato pelo nome
def buscar_contato(nome):
    for contato in contatos:
        if contato["Nome"] == nome:
            print("\nContato encontrado:")
            print("-" * 20)
            print(f"Nome: {contato['Nome']}")
            print(f"Telefone: {contato['Telefone']}")
            print(f"E-mail: {contato['E-mail']}")
            print("-" * 20)
            print("\n")
            return
    print("\nContato não encontrado.\n")

# Função para excluir um contato pelo nome
def excluir_contato(nome):
    for contato in contatos:
        if contato["Nome"] == nome:
            contatos.remove(contato)
            print("\nContato removido com sucesso!\n")
            return
    print("\nContato não encontrado.\n")

# Função principal
def main():
    while True:
        print("### Agenda de Contatos ###")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Buscar Contato")
        print("4. Excluir Contato")
        print("5. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("E-mail: ")
            adicionar_contato(nome, telefone, email)

        elif opcao == '2':
            listar_contatos()

        elif opcao == '3':
            nome = input("\nNome a ser buscado: ")
            buscar_contato(nome)

        elif opcao == '4':
            nome = input("\nNome a ser excluído: ")
            excluir_contato(nome)

        elif opcao == '5':
            print("\nEncerrando a Agenda de Contatos.\n")
            break

        else:
            print("\nOpção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()
