import random

class JogoNumeroPrimo:
    def __init__(self):
        self.pontuacao = 0

    def is_primo(self, numero):
        # Verifica se um número é primo. 
        # A função usa um intervalo de 2 até int(numero**0.5) + 1 para verificar a divisibilidade do número. 
        # Isso é uma otimização comumente usada na verificação de números primos. 
        # A ideia é que se um número não é primo, ele terá pelo menos um divisor que seja menor ou igual à sua raiz quadrada. 
        # Portanto, não é necessário verificar números maiores que a raiz quadrada do número. 
        # Isso economiza tempo de computação em casos onde o número é grande.
        if numero <= 1:
            return False
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True

    def jogar(self):
        while True:
            self.mostrar_menu()
            opcao = input("\nEscolha uma opção: ")

            if opcao == '1':
                self.jogar_rodada()
            elif opcao == '2':
                self.mostrar_pontuacao()
            elif opcao == '3':
                self.zerar_pontuacao()
            elif opcao == '4':
                print("\nObrigado por jogar. Até logo!\n")
                break
            else:
                print("\nOpção inválida.")

    def mostrar_menu(self):
        # Exibe o menu de opções.
        print("\n#######################################")
        print("Jogo do Número Primo")
        print("1. Jogar")
        print("2. Ver Pontuação")
        print("3. Zerar Pontuação")
        print("4. Sair")
        print("#######################################")

    def jogar_rodada(self):
        # Executa uma rodada do jogo.
        numero_gerado = random.randint(1, 100)
        print(f"\nNúmero gerado: {numero_gerado}")
        resposta = input("\nÉ primo (P) ou não primo (N)? ").strip().lower()

        if (resposta == 'p' and self.is_primo(numero_gerado)) or (resposta == 'n' and not self.is_primo(numero_gerado)):
            self.pontuacao += 1
            print(f"\nResposta correta! Sua pontuação: {self.pontuacao}")
        else:
            print("\nResposta incorreta. O jogo acabou.")

    def mostrar_pontuacao(self):
        # Mostra a pontuação atual.
        print(f"\nPontuação atual: {self.pontuacao}")

    def zerar_pontuacao(self):
        # Zera a pontuação.
        self.pontuacao = 0
        print("\nPontuação zerada.")

if __name__ == "__main__":
    jogo = JogoNumeroPrimo()
    jogo.jogar()
