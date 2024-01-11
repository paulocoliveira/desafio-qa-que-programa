# Solicita ao usuário que insira um número
numero_str = input("Digite um número: ")

# Esta linha utiliza a função input() para solicitar ao usuário que insira um número. 
# O texto "Digite um número: " é exibido como prompt, e a entrada fornecida pelo usuário é armazenada na variável numero_str como uma string.

# Converte a entrada do usuário para um número inteiro
numero = int(numero_str)

# Nesta linha, a função int() é usada para converter a string numero_str para um número inteiro. 
# Isso é necessário porque a entrada do usuário é tratada como texto (string) pelo input(), e queremos realizar operações matemáticas com esse número.


# Verifica se o número é par ou ímpar usando o operador de módulo (%)
if numero % 2 == 0:
    print(f"{numero} é um número par.")
else:
    print(f"{numero} é um número ímpar.")

# Aqui, utilizamos uma estrutura condicional if/else para verificar se o número é par ou ímpar. O operador de módulo % retorna o resto da divisão entre dois números. Se numero % 2 resultar em zero, significa que o número é divisível por 2 e, portanto, é par. Caso contrário, o número é ímpar.

# Se o número for par, o bloco de código dentro do if é executado, e uma mensagem indicando que o número é par é impressa.
# Se o número for ímpar, o bloco de código dentro do else é executado, e uma mensagem indicando que o número é ímpar é impressa.
# A utilização da f-string (f"{numero} é um número par.") facilita a formatação da string, incorporando o valor da variável numero na mensagem de saída.