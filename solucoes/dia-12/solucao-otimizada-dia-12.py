from collections import defaultdict

def analisar_frequencia_letras(texto):
    """Analisa a frequência das letras em um texto."""
    frequencia_letras = defaultdict(int)
    
    for caractere in texto:
        if caractere.isalpha():
            frequencia_letras[caractere.lower()] += 1
    
    return dict(frequencia_letras)

def main():
    """Função principal."""
    texto = input("Digite um texto: ")
    frequencia = analisar_frequencia_letras(texto)
    
    print("Frequência das letras:")
    for letra, frequencia in frequencia.items():
        print(f"{letra}: {frequencia}")

if __name__ == "__main__":
    main()
