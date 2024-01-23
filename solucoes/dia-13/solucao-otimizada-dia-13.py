import re  # Importa o módulo de expressões regulares

def validar_email(email):
    """Verifica se um e-mail é válido usando expressões regulares."""
    # Define um padrão de expressão regular para verificar um e-mail válido
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao, email) is not None

def main():
    """Função principal."""
    email = input("Digite um e-mail: ")
    
    if validar_email(email):
        print("E-mail válido")
    else:
        print("E-mail inválido")

if __name__ == "__main__":
    main()
