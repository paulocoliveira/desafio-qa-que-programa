# Esta função calcula o resultado de uma operação matemática básica entre dois números.
def calcular(op, n1, n2):
    # Verifica se a operação é divisão e o segundo número é zero.
    if op == "/" and n2 == 0:
        return "Não é possível dividir por zero"  # Retorna uma mensagem de erro para divisão por zero.

    # Um dicionário que mapeia uma string representando uma operação matemática ('+', '-', '*', '/')
    # para a função lambda correspondente que executa a operação.
    operacoes = {
        "+": lambda x, y: x + y,  # Adição: soma x e y.
        "-": lambda x, y: x - y,  # Subtração: subtrai y de x.
        "*": lambda x, y: x * y,  # Multiplicação: multiplica x por y.
        "/": lambda x, y: x / y   # Divisão: divide x por y.
    }
    # O método get é usado para obter a função lambda correspondente à operação fornecida ('op').
    # Se 'op' não for encontrado no dicionário, uma função lambda padrão é fornecida,
    # que retorna "Operação inválida.".
    # A função lambda selecionada é então chamada com n1 (x) e n2 (y) como argumentos.
    return operacoes.get(op, lambda x, y: "Operação inválida.")(n1, n2)

# Solicita ao usuário o primeiro número e o armazena na variável 'num1'.
num1 = float(input("Digite o primeiro número: "))

# Solicita ao usuário escolher a operação e a armazena na variável 'oper'.
oper = input("Escolha a operação (+, -, *, /): ")

# Solicita ao usuário o segundo número e o armazena na variável 'num2'.
num2 = float(input("Digite o segundo número: "))

# Chama a função 'calcular' com os números e a operação fornecidos e imprime o resultado.
print(f"Resultado: {calcular(oper, num1, num2)}")
