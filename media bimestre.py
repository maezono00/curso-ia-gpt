print("=" * 50)
print("\tBem vindo à calculadora de médias 2000!!! 🤓")
print("=" * 50)


biUm = float(input("Insira a primeira nota do bimestre: "))
biDois = float(input("Insira a segunda nota do bimestre: "))
biTres = float(input("Insira a terceira nota do bimestre: "))
biQuatro = float(input("Insira a quarta nota do bimestre: "))

media = (biUm + biDois + biTres + biQuatro) / 4

#print(f"\nA média do aluno é: {(notaUm + notaDois) / 2}")
#print(f"\nA média do aluno é: {media}")

if media >= 6:
    print(f"\nParabéns, sua média é {media}, você está aprovado! 🥳")
else:
    print(f"\nParabéns, sua média é {media}, você está reprovado!!! 😍")