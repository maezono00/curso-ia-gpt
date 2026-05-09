print("=" * 50)
print("\tBem vindo à calculadora de médias 2000!!! 🤓")
print("=" * 50)


notaUm = float(input("Insira a primeira nota do aluno: "))
notaDois = float(input("Insira a segunda nota do aluno: "))

media = (notaUm + notaDois) / 2

#print(f"\nA média do aluno é: {(notaUm + notaDois) / 2}")
#print(f"\nA média do aluno é: {media}")

if media >= 6:
    print("\nParabéns, você está aprovado! 🥳")
else:
    print("\nParabéns, você está reprovado!!! 😍")