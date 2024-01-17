import time  # Importa o módulo time

# Define uma função para limpar a linha anterior
def limpa_linha_anterior():
    print(' ' * 10, end='\r')  # Limpa a linha anterior

# Define uma função para o temporizador ou contador regressivo
def temporizador_contador(modo, tempo):
    if modo == '1':
        # Contagem progressiva do temporizador
        for segundo in range(1, tempo + 1):
            print(segundo, end='\r')
            time.sleep(1)
    elif modo == '2':
        # Contador regressivo
        for segundo in range(tempo, 0, -1):
            limpa_linha_anterior()
            print(segundo, end='\r')
            time.sleep(1)
    else:
        print("Escolha inválida.")
        return
    limpa_linha_anterior()
    print("\nTempo esgotado!")

# Solicita a escolha do usuário
print("Escolha o modo:\n1 - Temporizador\n2 - Regressivo")
modo_usuario = input("Digite 1 ou 2: ")

# Solicita o tempo do usuário
tempo_usuario = int(input("Digite o tempo (em segundos): "))

# Chama a função com a escolha do usuário
temporizador_contador(modo_usuario, tempo_usuario)
