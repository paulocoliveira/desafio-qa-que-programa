import random

class JogoAdivinhacao:
    def __init__(self):
        self.pontuacao = 0
        self.numero_minimo = 1
        self.numero_maximo = 100
        self.max_tentativas = 7

    def jogar(self):
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
                venceu, tentativas = self.jogar_rodada()
                if venceu:
                    self.pontuacao += 1
                    print(f"\nParabéns! Você acertou em {tentativas} tentativas.")
                    print(f"Sua pontuação atual: {self.pontuacao}")
                else:
                    print(f"\nVocê perdeu! O número correto era {self.numero_secreto}.")

            elif opcao == '2':
                print(f"\nPontuação atual: {self.pontuacao}")

            elif opcao == '3':
                self.zerar_pontuacao()

            elif opcao == '4':
                print("\nObrigado por jogar. Até logo!\n")
                break

            else:
                print("\nOpção inválida.")

    def jogar_rodada(self):
        self.numero_secreto = random.randint(self.numero_minimo, self.numero_maximo)
        tentativas = 0

        while tentativas < self.max_tentativas:
            tentativa = self.obter_tentativa()
            tentativas += 1

            if tentativa == self.numero_secreto:
                return True, tentativas
            elif tentativa < self.numero_secreto:
                print("\nO número correto é maior.")
            else:
                print("\nO número correto é menor.")

            print(f"Tentativas restantes: {self.max_tentativas - tentativas}")

        return False, tentativas

    def obter_tentativa(self):
        while True:
            try:
                tentativa = int(input(f"\nTente adivinhar o número ({self.numero_minimo} - {self.numero_maximo}): "))
                if self.numero_minimo <= tentativa <= self.numero_maximo:
                    return tentativa
                else:
                    print(f"Por favor, insira um número entre {self.numero_minimo} e {self.numero_maximo}.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")

    def zerar_pontuacao(self):
        self.pontuacao = 0
        print("\nPontuação zerada.")

if __name__ == "__main__":
    jogo = JogoAdivinhacao()
    jogo.jogar()
