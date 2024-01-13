# Desafio
#  Desenvolva um programa que peça ao usuário para inserir um número. O programa deve então verificar se o número é par ou ímpar e exibir uma mensagem informando o usuário.

numero = int(input("Informe um numero: "))
if numero %2 <= 0:
  print("O numero escolhido", numero,  "é Par")
else:
  print("O numero escolhido", numero,  "é impar")