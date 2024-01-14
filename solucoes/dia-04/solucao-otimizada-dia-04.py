import re  # Importa o módulo de expressões regulares

# Define uma função para contar palavras usando expressões regulares
def contar_palavras_regex(texto):
    # Utiliza a expressão regular '[^\s]+' para encontrar todas as sequências de caracteres
    # que não sejam espaços. '[^\s]' corresponde a qualquer caractere que não seja um espaço,
    # e '+' indica uma ou mais ocorrências
    palavras = re.findall(r'[^\s]+', texto)
    # Retorna a quantidade de palavras encontradas
    return len(palavras)

# Solicita a entrada do usuário
texto_usuario = input("Digite um texto: ")

# Chama a função contar_palavras_regex e imprime o resultado
print(f"O texto contém {contar_palavras_regex(texto_usuario)} palavras.")