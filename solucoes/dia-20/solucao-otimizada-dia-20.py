class Pergunta:
    def __init__(self, pergunta, opcoes, resposta):
        self.pergunta = pergunta
        self.opcoes = opcoes
        self.resposta = resposta

class Quiz:
    def __init__(self, perguntas):
        self.perguntas = perguntas
        self.pontuacao = 0

    def mostrar_pontuacao(self):
        print(f"\nSua pontuação final: {self.pontuacao}/{len(self.perguntas)}\n")

    def fazer_pergunta(self, pergunta):
        print(f"\nPergunta: {pergunta.pergunta}")

        # Exibe as opções
        for i, opcao in enumerate(pergunta.opcoes, 1):
            print(f"{chr(64 + i)}. {opcao}")

        resposta_correta = pergunta.resposta

        while True:
            resposta_usuario = input("\nSua resposta (A/B/C/D): ").upper()

            if resposta_usuario in ['A', 'B', 'C', 'D']:
                break
            else:
                print("Opção inválida. Escolha A, B, C ou D.")

        if resposta_usuario == resposta_correta:
            print("\nResposta correta!\n")
            self.pontuacao += 1
        else:
            print(f"\nResposta incorreta. A resposta correta é: {resposta_correta}\n")

    def executar_quiz(self):
        for i, pergunta in enumerate(self.perguntas, 1):
            self.fazer_pergunta(pergunta)

# Lista de perguntas, opções e respostas
perguntas = [
    Pergunta("Qual é a capital do Brasil?", ["Brasília", "São Paulo", "Rio de Janeiro", "Belo Horizonte"], "A"),
    Pergunta("Quem escreveu 'Dom Quixote'?", ["Miguel de Cervantes", "William Shakespeare", "Charles Dickens", "Jane Austen"], "A"),
    Pergunta("Qual é o maior planeta do sistema solar?", ["Vênus", "Terra", "Marte", "Júpiter"], "D")
]

# Cria um objeto Quiz e executa o quiz
quiz = Quiz(perguntas)
quiz.executar_quiz()

# Mostra a pontuação final
quiz.mostrar_pontuacao()
