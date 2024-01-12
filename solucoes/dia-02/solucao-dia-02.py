# Solicita ao usuário que insira o primeiro número
numero1 = float(input("Digite o primeiro número: "))  

# Solicita ao usuário que escolha a operação
operacao = input("Escolha a operação (+, -, *, /): ").lower()

# Solicita ao usuário que insira o segundo número
numero2 = float(input("Digite o segundo número: "))  

# Realiza a operação escolhida
if operacao == "+":
    resultado = numero1 + numero2  # Realiza a adição
elif operacao == "-":
    resultado = numero1 - numero2  # Realiza a subtração
elif operacao == "*":
    resultado = numero1 * numero2  # Realiza a multiplicação
elif operacao == "/":
    # Verifica se o segundo número é zero antes de realizar a divisão
    if numero2 == 0:
        resultado = "Não é possível dividir por zero"  # Mensagem de erro para divisão por zero
    else:
        resultado = numero1 / numero2  # Realiza a divisão
else:
    resultado = "Operação inválida."  # Mensagem de erro para operação inválida

print(f"Resultado: {resultado}")  # Imprime o resultado
