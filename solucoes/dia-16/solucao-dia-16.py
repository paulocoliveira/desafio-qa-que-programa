import random

# Lista de palavras para o jogo
palavras = ["python", "programacao", "desenvolvimento", "computador", "linguagem"]

# Escolhe uma palavra aleatoriamente
palavra_aleatoria = random.choice(palavras)

# Inicializa a palavra a ser adivinhada com underscores
palavra_adivinhar = ["_" for letra in palavra_aleatoria]

# Número máximo de tentativas
max_tentativas = 6

# Letras erradas
letras_erradas = []

# Letras já tentadas
letras_tentadas = []

while max_tentativas > 0:
    # Imprime a palavra a ser adivinhada
    print(" ".join(palavra_adivinhar))
    
    # Pede ao usuário para adivinhar uma letra
    letra = input("Digite uma letra: ").lower()

    # Verifica se a letra já foi tentada antes
    if letra in letras_tentadas:
        print("\nVocê já tentou essa letra antes. Tente novamente.\n")
        continue

    letras_tentadas.append(letra)

    # Verifica se a letra está na palavra
    if letra in palavra_aleatoria:
        for i in range(len(palavra_aleatoria)):
            if palavra_aleatoria[i] == letra:
                palavra_adivinhar[i] = letra
    else:
        letras_erradas.append(letra)
        max_tentativas -= 1
        print(f"Tentativas restantes: {max_tentativas}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")

    # Verifica se o jogador ganhou
    if "_" not in palavra_adivinhar:
        print("\nParabéns! Você ganhou.\n")
        break

# Verifica se o jogador perdeu
if max_tentativas == 0:
    print("\nVocê perdeu. A palavra era: " + palavra_aleatoria + "\n")
