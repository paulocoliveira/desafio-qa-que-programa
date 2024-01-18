def mostrar_tarefas(tarefas):
    # Exibe a lista de tarefas.
    if len(tarefas) > 0:
        print("\nLista de Tarefas:")
        for indice, tarefa in enumerate(tarefas):
            print(f"{indice}. {tarefa}")
    else:
        print("\nLista de tarefas vazia!")

def adicionar_tarefa(tarefas):
    # Adiciona uma nova tarefa à lista.
    tarefa = input("\nDigite a tarefa a ser adicionada: ")
    tarefas.append(tarefa)
    print("\nTarefa adicionada.")

def remover_tarefa(tarefas):
    # Mostra a lista de tarefas com índices
    if(len(tarefas) > 0):
        print("\nLista de Tarefas:")
        for indice, tarefa in enumerate(tarefas):
            print(f"{indice}: {tarefa}")
        
        # Solicita o índice da tarefa a ser removida
        indice = int(input("\nDigite o número da tarefa a ser removida: "))
        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)  # Remove a tarefa da lista
            print("\nTarefa removida.")
        else:
            print("\nÍndice inválido.")
    else:
        print("\n Lista de tarefas vazia!")

def main():
    # Função principal que executa o gerenciador de lista de tarefas.
    tarefas = []

    while True:
    # Exibe o menu de opções
        print("\n#######################################")
        print("Gerenciador de Lista de Tarefas")
        print("1. Adicionar tarefa")
        print("2. Remover tarefa")
        print("3. Mostrar tarefas")
        print("4. Sair")
        print("#######################################")
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            adicionar_tarefa(tarefas)
        elif opcao == '2':
            remover_tarefa(tarefas)
        elif opcao == '3':
            mostrar_tarefas(tarefas)
        elif opcao == '4':
            print("\nObrigado por usar o gerenciador de tarefas. Até logo!\n")
            break
        else:
            print("\nOpção inválida.")

if __name__ == "__main__":
    main()
