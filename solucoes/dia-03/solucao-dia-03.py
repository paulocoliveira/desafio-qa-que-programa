# Solicita ao usuário que insira uma palavra ou frase
texto = input("Digite uma palavra ou frase: ")

# Remove espaços, vírgulas, interrogações, exclamações e pontos e converte o texto para minúsculas para padronização
texto_formatado = texto.replace(" ", "")
texto_formatado = texto_formatado.replace(",", "")
texto_formatado = texto_formatado.replace(".", "")
texto_formatado = texto_formatado.replace("!", "")
texto_formatado = texto_formatado.replace("?", "")
texto_formatado = texto_formatado.lower()

# Variável para armazenar a versão invertida do texto
texto_invertido = ""

# Inverte o texto_formatado usando um loop
for caractere in texto_formatado:
    texto_invertido = caractere + texto_invertido

# Verifica se o texto formatado é igual ao texto invertido
if texto_formatado == texto_invertido:
    resultado = "É um palíndromo."  # Mensagem para palíndromo
else:
    resultado = "Não é um palíndromo."  # Mensagem para não palíndromo

print(resultado)  # Imprime o resultado
