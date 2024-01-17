import time  # Importa o módulo time

# Solicita ao usuário para escolher entre temporizador e contador regressivo
print("Escolha o modo:\n1 - Temporizador\n2 - Regressivo")
escolha = input("Digite 1 ou 2: ")

# Solicita ao usuário o tempo (em segundos)
tempo = int(input("Digite o tempo (em segundos): "))

if escolha == '1':
    # Contagem progressiva do temporizador
    contador = 0
    while contador < tempo:
        print(contador + 1, end='\r')
        time.sleep(1)
        contador += 1
elif escolha == '2':
    # Contador regressivo
    while tempo > 0:
        print(' ' * 10, end='\r')  # Limpa a linha anterior
        print(tempo, end='\r')
        time.sleep(1)
        tempo -= 1
else:
    print("Escolha inválida.")

print(' ' * 10, end='\r')  # Limpa a linha anterior
print("\nTempo esgotado!")

