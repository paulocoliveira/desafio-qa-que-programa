# Solicita ao usuário que insira um texto
texto = input("Digite um texto: ")

# Usa a função split() para dividir o texto em palavras, baseando-se nos espaços
palavras = texto.split()

# Conta o número de palavras usando a função len() que retorna o tamanho da lista
contagem = len(palavras)

print(f"O texto contém {contagem} palavras.")  # Imprime o número de palavras
