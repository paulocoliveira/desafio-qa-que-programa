import csv

def adicionar_livro():
    titulo = input("\nDigite o título do livro: ")
    autor = input("\nDigite o autor do livro: ")
    ano = input("\nDigite o ano de publicação do livro: ")

    with open('biblioteca1.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([titulo, autor, ano])
    
    print("\nLivro adicionado com sucesso!")

def visualizar_biblioteca():
    try:
        with open('biblioteca1.csv', mode='r') as file:
            reader = csv.reader(file)
            print("\nLista de Livros na Biblioteca:")
            for row in reader:
                print(f"Título: {row[0]}, Autor: {row[1]}, Ano: {row[2]}")
    except FileNotFoundError:
        print("\nA biblioteca está vazia.")

while True:
    print("\n### Gerenciador de Biblioteca Pessoal ###")
    print("1. Adicionar livro")
    print("2. Visualizar biblioteca")
    print("3. Sair")
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == '1':
        adicionar_livro()
    elif opcao == '2':
        visualizar_biblioteca()
    elif opcao == '3':
        print("\nObrigado por usar o Gerenciador de Biblioteca Pessoal!\n")
        break
    else:
        print("\nOpção inválida. Tente novamente.")
