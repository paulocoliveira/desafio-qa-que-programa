class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone, email):
        contato = Contato(nome, telefone, email)
        self.contatos.append(contato)
        print("\nContato adicionado com sucesso!\n")

    def listar_contatos(self):
        if not self.contatos:
            print("\nA agenda está vazia.\n")
        else:
            print("\nLista de Contatos:")
            print("-" * 20)
            for contato in self.contatos:
                self.exibir_contato(contato)
            print("\n")

    def buscar_contato(self, nome):
        encontrado = False
        for contato in self.contatos:
            if contato.nome == nome:
                print("-" * 20)
                self.exibir_contato(contato)
                encontrado = True
                break
        if not encontrado:
            print("\nContato não encontrado.\n")

    def excluir_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                print("\nContato removido com sucesso!\n")
                return
        print("\nContato não encontrado.\n")

    def exibir_contato(self, contato):
        print(f"Nome: {contato.nome}")
        print(f"Telefone: {contato.telefone}")
        print(f"E-mail: {contato.email}")
        print("-" * 20)

def main():
    agenda = Agenda()

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
            agenda.adicionar_contato(nome, telefone, email)

        elif opcao == '2':
            agenda.listar_contatos()

        elif opcao == '3':
            nome = input("\nNome a ser buscado: ")
            agenda.buscar_contato(nome)

        elif opcao == '4':
            nome = input("\nNome a ser excluído: ")
            agenda.excluir_contato(nome)

        elif opcao == '5':
            print("\nEncerrando a Agenda de Contatos.\n")
            break

        else:
            print("\nOpção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()
