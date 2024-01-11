# Solicita ao usuário que insira um número e armazena o valor na variável 'numero'
numero = int(input("Digite um número: "))  

# Verifica se o número é par usando o operador de módulo
# Se o resto da divisão do número por 2 for 0, o número é par
if numero % 2 == 0:  
    print("O número é par.")  # Imprime uma mensagem dizendo que o número é par
else:
    print("O número é ímpar.")  # Se não for par, imprime que o número é ímpar
