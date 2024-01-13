# Define uma função para verificar palíndromos
def verificar_palindromo(texto):
    # Formata o texto removendo espaços e convertendo para minúsculas
    texto = texto.replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "").lower()
    # Retorna True se o texto é igual ao seu inverso, caso contrário False
    return texto == texto[::-1]

# Solicita a entrada do usuário
texto_usuario = input("Digite uma palavra ou frase: ")

# Verifica se o texto é um palíndromo e imprime o resultado
print("É um palíndromo." if verificar_palindromo(texto_usuario) else "Não é um palíndromo.")
