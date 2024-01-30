class Quiz:
    def __init__(self, perguntas):
        self.perguntas = perguntas
        self.pontuacao = 0

    def mostrar_pergunta(self, pergunta, opcoes):
        print(pergunta)
        for i, opcao in enumerate(opcoes, 1):
            print(f"{chr(64 + i)}. {opcao}")

    def executar_quiz(self):
        for i, pergunta in enumerate(self.perguntas, 1):
            print(f"\nPergunta {i}:")
            self.mostrar_pergunta(pergunta["pergunta"], pergunta["opcoes"])
            resposta_usuario = input("\nSua resposta (A/B/C/D): ").upper()

            if resposta_usuario == pergunta["resposta"]:
                print("\nResposta correta!\n")
                self.pontuacao += 1
            else:
                print(f"\nResposta incorreta. A resposta correta é: {pergunta['resposta']}\n")

    def mostrar_pontuacao(self):
        print(f"\nSua pontuação final: {self.pontuacao}/{len(self.perguntas)}\n")

# Lista de perguntas, opções e respostas
perguntas = [
    {
        "pergunta": "Qual é a capital do Brasil?",
        "opcoes": ["Brasília", "São Paulo", "Rio de Janeiro", "Belo Horizonte"],
        "resposta": "A"
    },
    {
        "pergunta": "Quem escreveu 'Dom Quixote'?",
        "opcoes": ["Miguel de Cervantes", "William Shakespeare", "Charles Dickens", "Jane Austen"],
        "resposta": "A"
    },
    {
        "pergunta": "Qual é o maior planeta do sistema solar?",
        "opcoes": ["Vênus", "Terra", "Marte", "Júpiter"],
        "resposta": "D"
    }
]

# Cria um objeto Quiz e executa o quiz
quiz = Quiz(perguntas)
quiz.executar_quiz()

# Mostra a pontuação final
quiz.mostrar_pontuacao()
