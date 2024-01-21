# Solicita que o usuário insira os números separados por espaço
entrada = input("Insira os números separados por espaço: ")

# Divide a entrada em uma lista de strings
numeros_str = entrada.split()

# Converte os números para inteiros
numeros = [int(numero) for numero in numeros_str]

# Ordena a lista de números
numeros_ordenados = sorted(numeros)

# Imprime a lista ordenada
print("Lista ordenada:", numeros_ordenados)