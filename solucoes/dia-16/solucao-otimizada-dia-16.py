import random

def escolher_palavra():
    palavras = ["python", "programacao", "desenvolvimento", "computador", "linguagem"]
    return random.choice(palavras)

def inicializar_palavra(palavra):
    return ["_" for letra in palavra]

def adivinhar_letra(palavra_aleatoria, palavra_adivinhar, letras_tentadas, letras_erradas, max_tentativas):
    letra = input("Digite uma letra: ").lower()

    if letra in letras_tentadas:
        print("\nVocê já tentou essa letra antes. Tente novamente.\n")
        return max_tentativas

    letras_tentadas.add(letra)

    if letra in palavra_aleatoria:
        for i, letra_palavra in enumerate(palavra_aleatoria):
            if letra_palavra == letra:
                palavra_adivinhar[i] = letra
    else:
        letras_erradas.add(letra)
        max_tentativas -= 1
        print(f"Tentativas restantes: {max_tentativas}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")

    return max_tentativas

def main():
    palavra_aleatoria = escolher_palavra()
    palavra_adivinhar = inicializar_palavra(palavra_aleatoria)
    max_tentativas = 6
    letras_erradas = set()
    letras_tentadas = set()

    while max_tentativas > 0:
        print(" ".join(palavra_adivinhar))
        max_tentativas = adivinhar_letra(palavra_aleatoria, palavra_adivinhar, letras_tentadas, letras_erradas, max_tentativas)

        if "_" not in palavra_adivinhar:
            print("\nParabéns! Você ganhou.\n")
            break

    if max_tentativas == 0:
        print("\nVocê perdeu. A palavra era: " + palavra_aleatoria + "\n")

if __name__ == "__main__":
    main()
