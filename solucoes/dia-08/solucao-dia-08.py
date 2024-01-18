# Lista inicial de tarefas
lista_de_tarefas = []

# Loop principal do programa
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

    # Opção para adicionar tarefa
    if opcao == '1':
        tarefa = input("Digite a tarefa a ser adicionada: ")
        lista_de_tarefas.append(tarefa)  # Adiciona a tarefa à lista
        print("\nTarefa adicionada.")

    # Opção para remover tarefa
    elif opcao == '2':
        # Mostra a lista de tarefas com índices
        if(len(lista_de_tarefas) > 0):
            print("\nLista de Tarefas:")
            for indice, tarefa in enumerate(lista_de_tarefas):
                print(f"{indice}: {tarefa}")
            
            # Solicita o índice da tarefa a ser removida
            indice = int(input("\nDigite o número da tarefa a ser removida: "))
            if 0 <= indice < len(lista_de_tarefas):
                lista_de_tarefas.pop(indice)  # Remove a tarefa da lista
                print("\nTarefa removida.")
            else:
                print("\nÍndice inválido.")
        else:
            print("\n Lista de tarefas vazia!")

    # Opção para mostrar tarefas
    elif opcao == '3':
        if(len(lista_de_tarefas) > 0):
            print("\nLista de Tarefas:")
            for indice, tarefa in enumerate(lista_de_tarefas):
                print(f"{indice}: {tarefa}")
        else:
            print("\n Lista de tarefas vazia!")

    # Opção para sair do programa
    elif opcao == '4':
        print("\nObrigado por usar o gerenciador de tarefas. Até logo!\n")
        break

    # Opção inválida
    else:
        print("\nOpção inválida.")
