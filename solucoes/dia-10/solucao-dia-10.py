import random  # Importa o módulo random para gerar números aleatórios

def jogar_jogo():
    pontuacao = 0  # Inicializa a pontuação do jogador

    while True:
        print("\n#######################################")
        print("Jogo da Adivinhação")
        print("1. Jogar")
        print("2. Ver Pontuação")
        print("3. Zerar Pontuação")
        print("4. Sair")
        print("#######################################")
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            numero_secreto = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100
            tentativas = 0  # Inicializa o contador de tentativas
            venceu = False  # Variável para verificar se o jogador acertou

            while tentativas < 7:
                tentativa = int(input("\nTente adivinhar o número (entre 1 e 100): "))
                tentativas += 1

                if tentativa == numero_secreto:
                    venceu = True
                    break
                elif tentativa < numero_secreto:
                    print("\nO número correto é maior.")
                else:
                    print("\nO número correto é menor.")

                print("Tentativas restantes: " + str(7 - tentativas))

            if venceu:
                pontuacao += 1
                print(f"\nParabéns! Você acertou em {tentativas} tentativas.")
                print(f"Sua pontuação atual: {pontuacao}")
            else:
                print(f"\nVocê perdeu! O número correto era {numero_secreto}.")

        elif opcao == '2':
            print(f"\nPontuação atual: {pontuacao}")

        elif opcao == '3':
            pontuacao = 0
            print("\nPontuação zerada.")

        elif opcao == '4':
            print("\nObrigado por jogar. Até logo!\n")
            break

        else:
            print("\nOpção inválida.")

if __name__ == "__main__":
    jogar_jogo()
