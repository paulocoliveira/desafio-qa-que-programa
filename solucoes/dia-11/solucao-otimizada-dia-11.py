def ordenar_lista(lista):
    """Ordena uma lista de números."""
    return sorted(lista)

def main():
    """Função principal."""
    numeros = [int(numero) for numero in input("Insira os números separados por espaço: ").split()]
    print("Lista ordenada:", ordenar_lista(numeros))

if __name__ == "__main__":
    main()
