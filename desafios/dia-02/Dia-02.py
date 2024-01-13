while True:
    print("\nSelecione uma opção para começar:")
    print("1- Soma")
    print("2- Divisão")
    print("3- Multiplicação")
    print("4- Subtração")
    print("5- Sair")

    opcao = int(input("Informe a opção desejada: "))
    if opcao == 1:
        soma1 = int(input("Informe o primeiro numeros a ser somado: "))
        soma2 = int(input("Informe o segundo numeros a ser somado: "))
        resultado_soma = soma1 + soma2
        print("O resultado da soma de " ,soma1, "+", soma2, "é igual a: ", resultado_soma)
    elif opcao == 2:
        divisao1 = int(input("Informe o primeiro numero: "))
        divisao2 = int(input("Informe o segundo numero: "))
        if divisao2 != 0:
          resultado_divisao = float(divisao1 / divisao2)
          print(f"O resultado da divisão de {divisao1} por {divisao2} é igual a: {resultado_divisao:.2f}")
        else:
          print("Erro: Divisão por zero não é permitida.")
    elif opcao == 3:
        multiplicacao1 = int(input("Informe o primeiro numero: "))
        multiplicacao2 = int(input("Informe o segundo numero: "))
        resultado_multiplicacao = int(multiplicacao1*multiplicacao2)
        print("O resultado da multiplicacao de:", multiplicacao1, "por", multiplicacao2, "é igual a: ", resultado_multiplicacao)
    elif opcao == 4:
        substracao1 = int(input("Informe o primeiro numero: "))
        substracao2 = int(input("Informe o segundo numero: "))
        resultado_substracao = int(substracao1 - substracao2)
        print("O resusltado da subtração de:", substracao1, "-", substracao2, "é igual a: ", resultado_substracao)
    elif opcao == 5:
          print("Saindo do programa. Até logo!")
          break  # Encerra o loop quando o usuário escolhe a opção de sair

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")