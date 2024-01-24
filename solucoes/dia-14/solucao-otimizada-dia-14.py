import random
import string

def obter_caracteres(usar_numeros, usar_maiusculas, usar_minusculas, usar_especiais):
    caracteres = ""
    
    if usar_numeros:
        caracteres += string.digits
    
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    
    if usar_especiais:
        caracteres += string.punctuation
    
    return caracteres

def gerar_senha(comprimento, usar_numeros, usar_maiusculas, usar_minusculas, usar_especiais):
    caracteres = obter_caracteres(usar_numeros, usar_maiusculas, usar_minusculas, usar_especiais)
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

# Solicita os critérios ao usuário
comprimento = int(input("Comprimento da senha: "))
usar_numeros = input("Usar números (S/N)? ").strip().lower() == 's'
usar_maiusculas = input("Usar letras maiúsculas (S/N)? ").strip().lower() == 's'
usar_minusculas = input("Usar letras minúsculas (S/N)? ").strip().lower() == 's'
usar_especiais = input("Usar caracteres especiais (S/N)? ").strip().lower() == 's'

# Gera a senha e imprime
senha = gerar_senha(comprimento, usar_numeros, usar_maiusculas, usar_minusculas, usar_especiais)
print("\nSenha gerada:", senha)
