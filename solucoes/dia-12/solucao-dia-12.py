# Solicita ao usuário que insira um texto
texto = input("Digite um texto: ")

# Inicializa um dicionário vazio para rastrear a frequência das letras
frequencia_letras = {}

# Itera sobre cada caractere no texto
for caractere in texto:
    # Verifica se o caractere é uma letra
    if caractere.isalpha():
        # Converte o caractere para minúsculas para evitar diferenciação entre maiúsculas e minúsculas
        caractere = caractere.lower()
        # Atualiza a contagem do caractere no dicionário
        frequencia_letras[caractere] = frequencia_letras.get(caractere, 0) + 1

# Imprime a frequência das letras
print("Frequência das letras:")
for letra, frequencia in frequencia_letras.items():
    print(f"{letra}: {frequencia}")
