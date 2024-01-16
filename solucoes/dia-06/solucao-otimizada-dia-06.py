# Define uma função para converter unidades
def converter_unidades(opcao, valor):
    # Dicionário com as funções de conversão
    conversoes = {
        '1': lambda v: v * 0.621371,  # Quilômetros para Milhas
        '2': lambda v: v * 1.60934,   # Milhas para Quilômetros
        '3': lambda v: v * 3.28084,   # Metros para Pés
        '4': lambda v: v * 0.3048,    # Pés para Metros
        '5': lambda v: v * 9/5 + 32,  # Celsius para Fahrenheit
        '6': lambda v: (v - 32) * 5/9 # Fahrenheit para Celsius
    }
    # Retorna o resultado da conversão
    return conversoes.get(opcao, lambda v: "Opção inválida")(valor)

# Solicita ao usuário que escolha a conversão
opcao_usuario = input("Escolha a conversão: \n1. Quilômetros para Milhas \n2. Milhas para Quilômetros \n3. Metros para Pés \n4. Pés para Metros \n5. Celsius para Fahrenheit \n6. Fahrenheit para Celsius \nDigite o número da opção: ")

# Solicita ao usuário que insira o valor a ser convertido
valor_usuario = float(input("Digite o valor a ser convertido: "))

# Realiza a conversão e imprime o resultado
print(f"Resultado da conversão: {converter_unidades(opcao_usuario, valor_usuario)}")