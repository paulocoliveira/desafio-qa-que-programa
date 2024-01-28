import requests

# Função para fazer a conversão de moedas
def converter_moeda(valor, moeda_origem, moeda_destino):
    # URL da API de conversão de moedas
    url = f"https://open.er-api.com/v6/latest/{moeda_origem}"
    
    try:
        # Faz a requisição HTTP para obter as taxas de câmbio
        resposta = requests.get(url)
        dados = resposta.json()

        # Verifica se a moeda de origem é válida
        if dados["result"] == "error":
            return "\nMoeda de origem inválida.\n"

        # Verifica se a moeda de destino é válida
        if moeda_destino not in dados["rates"]:
            return "\nMoeda de destino inválida.\n"

        # Verifica se o valor é válido (deve ser um número positivo)
        if valor <= 0:
            return "\nValor inválido.\n"

        # Calcula a taxa de conversão e o valor convertido
        taxa_conversao = dados["rates"][moeda_destino]
        valor_convertido = valor * taxa_conversao
        return f"\nResultado da conversão: {valor_convertido:.2f} {moeda_destino}\n"

    except requests.exceptions.RequestException:
        return "\nErro na conexão com a API.\n"
    except ValueError:
        return "\nValor inválido.\n"

# Função principal
def main():
    print("\n### Conversor de Moedas ###\n")
    
    # Solicita os dados ao usuário
    valor = input("Digite o valor a ser convertido: ")
    try:
        valor = float(valor)
    except ValueError:
        print("\nValor inválido.\n")
        return

    moeda_origem = input("Digite a moeda de origem (por exemplo, USD): ").upper()
    moeda_destino = input("Digite a moeda de destino (por exemplo, EUR): ").upper()

    # Chama a função de conversão e imprime o resultado
    resultado = converter_moeda(valor, moeda_origem, moeda_destino)
    print(resultado)

if __name__ == "__main__":
    main()
