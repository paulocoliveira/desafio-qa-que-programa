# Dia 18: Conversor de Moedas

## Desafio
Desenvolva um programa que converta valores entre diferentes moedas. O programa deve permitir ao usuário inserir o valor, a moeda de origem e a moeda de destino, e então mostrar o valor convertido utilizando uma api pública que traz a taxa para a conversão.

## Quais conhecimentos eu preciso adquirir para resolver este desafio?
- Requisições HTTP em Python: Aprenda a fazer requisições a uma API de conversão de moedas.
- Manipulação de JSON em Python: Entenda como processar a resposta JSON da API.
- Estruturas de controle (if, else, loops): Use estruturas de controle para gerenciar o fluxo do programa.
- Funções de entrada e saída: Conheça as funções para obter a entrada do usuário e exibir a saída.

## Dica importante
- Pesquise e escolha uma API confiável de conversão de moedas para usar em seu programa. Podes utilizar a Exchange Rate API disponível em https://www.exchangerate-api.com/docs/free que apenas precisas fazer uma requisição para este endpoint https://open.er-api.com/v6/latest/MOEDABASE e na resposta vai ter as taxas de conversão para você fazer os cálculos.
- Certifique-se de que o usuário possa selecionar a moeda de origem e a moeda de destino e inserir o valor a ser convertido.
- Lide com erros ou situações excepcionais, como valores de moeda inválidos ou problemas de conexão com a API.

## Testes

Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

```
python nome-do-seu-script.py
```

Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

```
Após criar o seu código, você pode realizar alguns testes em seu programa. Certifique-se de que ele se comporte como esperado para diferentes valores de entrada. Aqui estão alguns exemplos de testes:

TESTE 01: Teste de conversão de moeda
Valor: 100
Moeda de origem: USD (Dólar Americano)
Moeda de destino: EUR (Euro)
Resultado esperado: O programa deve converter 100 dólares em euros e exibir o valor convertido.

TESTE 02: Teste de conversão de moeda
Valor: 1500
Moeda de origem: BRL (Reais)
Moeda de destino: EUR (Euro)
Resultado esperado: O programa deve converter 1500 reais em euros e exibir o valor convertido.

TESTE 03: Teste com moeda de origem inválida
Valor: 50
Moeda de origem: XYZ (Moeda inválida)
Moeda de destino: EUR (Euro)
Resultado esperado: O programa deve lidar com a situação de moeda de origem inválida e fornecer uma mensagem de erro apropriada.

TESTE 04: Teste com moeda de destino inválida
Valor: 75
Moeda de origem: USD (Dólar Americano)
Moeda de destino: XYZ (Moeda inválida)
Resultado esperado: O programa deve lidar com a situação de moeda de destino inválida e fornecer uma mensagem de erro apropriada.

TESTE 05: Teste com valor inválido
Valor: ABC (Valor inválido)
Moeda de origem: USD (Dólar Americano)
Moeda de destino: EUR (Euro)
Resultado esperado: O programa deve lidar com a situação de valor inválido e fornecer uma mensagem de erro apropriada.
```

Você pode fazer outros testes caso ache necessário.

## Concluiu?

Ao finalizar o seu desafio, não esqueça de voltar lá no grupo, na mensagem que enviei de manhã com este link, e curtir com um ✅.

Parabéns!!! Amanhã tem mais! 