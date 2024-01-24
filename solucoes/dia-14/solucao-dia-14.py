import random
import string

# Solicita o comprimento da senha ao usuário
comprimento = int(input("Comprimento da senha: "))
usar_numeros = input("Usar números (S/N)? ").strip().lower() == 's'
usar_maiusculas = input("Usar letras maiúsculas (S/N)? ").strip().lower() == 's'
usar_minusculas = input("Usar letras minúsculas (S/N)? ").strip().lower() == 's'
usar_especiais = input("Usar caracteres especiais (S/N)? ").strip().lower() == 's'

# Geração de senhas aleatórias
caracteres = ""

if usar_numeros:
    caracteres += string.digits

if usar_maiusculas:
    caracteres += string.ascii_uppercase

if usar_minusculas:
    caracteres += string.ascii_lowercase

if usar_especiais:
    caracteres += string.punctuation

senha = ''.join(random.choice(caracteres) for _ in range(comprimento))

print("\nSenha gerada:", senha)
