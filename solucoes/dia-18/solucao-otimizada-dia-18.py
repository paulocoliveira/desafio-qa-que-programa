import requests

# Função para obter as taxas de câmbio da API
def obter_taxas_de_cambio(moeda_origem):
    url = f"https://open.er-api.com/v6/latest/{moeda_origem}"
    try:
        resposta = requests.get(url)
        return resposta.json()
    except requests.exceptions.RequestException:
        return "Erro na conexão com a API."

# Função para converter moeda
def converter_moeda(valor, moeda_origem, moeda_destino):
    try:
        dados = obter_taxas_de_cambio(moeda_origem)

        # Verifica se a moeda de origem é válida
        if dados["result"] == "error":
            return "\nMoeda de origem inválida.\n"
        
        if moeda_destino not in dados["rates"]:
            return "\nMoeda de destino inválida.\n"

        if valor <= 0:
            return "\nValor inválido.\n"

        taxa_conversao = dados["rates"][moeda_destino]
        valor_convertido = valor * taxa_conversao
        return f"\nResultado da conversão: {valor_convertido:.2f} {moeda_destino}\n"
    except Exception as e:
        return "Erro no processo de conversão!"

# Função principal
def main():
    print("\n### Conversor de Moedas ###\n")
    
    # Solicita os dados ao usuário
    try:
        valor = float(input("Digite o valor a ser convertido: "))
        moeda_origem = input("Digite a moeda de origem (por exemplo, USD): ").upper()
        moeda_destino = input("Digite a moeda de destino (por exemplo, EUR): ").upper()

        resultado = converter_moeda(valor, moeda_origem, moeda_destino)
        print(resultado)
    except Exception as e:
        print("\nValor inválido.\n")

if __name__ == "__main__":
    main()
