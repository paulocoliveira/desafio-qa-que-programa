import re  # Importa o módulo de expressões regulares

def validar_email(email):
    # Define um padrão de expressão regular para verificar um e-mail válido
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Usa a função re.match() para verificar se o e-mail corresponde ao padrão
    if re.match(padrao, email):
        return True  # O e-mail é válido
    else:
        return False  # O e-mail é inválido

# Solicita ao usuário que insira um e-mail
email = input("Digite um e-mail: ")

# Chama a função validar_email() e verifica se o e-mail é válido
if validar_email(email):
    print("E-mail válido")
else:
    print("E-mail inválido")
