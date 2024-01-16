# Solicita ao usuário que escolha a conversão que deseja realizar
opcao = input("Escolha a conversão: \n1. Quilômetros para Milhas \n2. Milhas para Quilômetros \n3. Metros para Pés \n4. Pés para Metros \n5. Celsius para Fahrenheit \n6. Fahrenheit para Celsius \nDigite o número da opção: ")

# Solicita ao usuário que insira o valor a ser convertido
valor = float(input("Digite o valor a ser convertido: "))

# Realiza a conversão com base na opção escolhida
if opcao == '1':
    # Converte Quilômetros para Milhas
    convertido = valor * 0.621371
elif opcao == '2':
    # Converte Milhas para Quilômetros
    convertido = valor * 1.60934
elif opcao == '3':
    # Converte Metros para Pés
    convertido = valor * 3.28084
elif opcao == '4':
    # Converte Pés para Metros
    convertido = valor * 0.3048
elif opcao == '5':
    # Converte Celsius para Fahrenheit
    convertido = valor * 9/5 + 32
elif opcao == '6':
    # Converte Fahrenheit para Celsius
    convertido = (valor - 32) * 5/9
else:
    print("Opção inválida.")

print(f"Resultado da conversão: {convertido}")