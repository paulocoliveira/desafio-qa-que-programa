import random  # Importa o módulo random para gerar números aleatórios

def is_primo(numero):
    # Verifica se um número é primo.
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def jogar_jogo():
    # Função principal do jogo.
    pontuacao = 0  # Inicializa a pontuação do jogador

    while True:
        print("\n#######################################")
        print("Jogo do Número Primo")
        print("1. Jogar")
        print("2. Ver Pontuação")
        print("3. Zerar Pontuação")
        print("4. Sair")
        print("#######################################")
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            numero_gerado = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100
            print(f"\nNúmero gerado: {numero_gerado}")
            resposta = input("\nÉ primo (P) ou não primo (N)? ").strip().lower()

            if (resposta == 'p' and is_primo(numero_gerado)) or (resposta == 'n' and not is_primo(numero_gerado)):
                pontuacao += 1
                print(f"\nResposta correta! Sua pontuação: {pontuacao}")
            else:
                print("\nResposta incorreta. O jogo acabou.")
                break

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
