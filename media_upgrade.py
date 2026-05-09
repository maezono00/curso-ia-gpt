listaNotas = [] #os [] servem para criar uma lista vazia

print("=" * 50)
print("Bem vindo ao sistema de notas e médias 3000 🤖")
print("=" * 50)

while True:
    notas = input("Digite a nota que deseja inserir (escreva SAIR para parar.): ")
    #o .lower() vai converter tudo o que foi inserido como string para minúsculo. em contra partida, .upper() vai converter tudo para caixa alta.
    if notas.lower() == "sair":
        break
    else:
        #por padrão, por não ter declarado o tipo da variável, "notas" será só string.
        listaNotas.append(float(notas)) #.append serve para inserir dados em uma lista.

#print(listaNotas)
#o comando sum() vai somar todos os elementos da lista.
#o comando len() vai definir a quantidade de elementos estão na lista.
media = sum(listaNotas) / len(listaNotas)

#O :.2f vai limitar a saída de até 2 dígitos decimais.
if media >= 6:
    print(f"A média final do aluno é: {media:.2f}. O aluno está aprovado! 🥳")
else:
    print(f"A média final do aluno é: {media:.2f}. O aluno está reprovado! 🥳")    