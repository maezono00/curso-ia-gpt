#Desafio 3: Calculadora
# Enunciado:
# Vamos criar uma mini-calculadora de soma. Siga estes passos:
# Peça para o usuário digitar o primeiro número e guarde em uma variável.
# Peça para o usuário digitar o segundo número e guarde em uma variável.
# Crie uma variável que receba a soma das duas variáveis anteriores.
# Imprima o resultado na tela.

print("CALCULADORA 🧮")

valorUm = float(input("Insira um número qualquer: "))
valorDois = float(input("Insira outro número qualquer: "))
valorSoma = (valorUm + valorDois)

print(f"\nA soma dos valores inseridos é: {valorSoma:.2f}")