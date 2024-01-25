import csv

def adicionar_livro(titulo, autor, ano, biblioteca):
    biblioteca.append({'titulo': titulo, 'autor': autor, 'ano': ano})

def visualizar_biblioteca(biblioteca):
    if not biblioteca:
        print("\nA biblioteca está vazia.")
    else:
        print("\nLista de Livros na Biblioteca:")
        for livro in biblioteca:
            print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")

def salvar_biblioteca(biblioteca):
    with open('biblioteca2.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['titulo', 'autor', 'ano'])
        writer.writeheader()
        writer.writerows(biblioteca)

def carregar_biblioteca():
    try:
        with open('biblioteca2.csv', mode='r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []

biblioteca = carregar_biblioteca()

while True:
    print("\n### Gerenciador de Biblioteca Pessoal ###")
    print("1. Adicionar livro")
    print("2. Visualizar biblioteca")
    print("3. Sair")
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == '1':
        titulo = input("\nDigite o título do livro: ")
        autor = input("\nDigite o autor do livro: ")
        ano = input("\nDigite o ano de publicação do livro: ")
        adicionar_livro(titulo, autor, ano, biblioteca)
        salvar_biblioteca(biblioteca)
        print("\nLivro adicionado com sucesso!")
    elif opcao == '2':
        visualizar_biblioteca(biblioteca)
    elif opcao == '3':
        print("\nObrigado por usar o Gerenciador de Biblioteca Pessoal!\n")
        break
    else:
        print("\nOpção inválida. Tente novamente.")
