#AULA 09/05/2026
#INTRODUÇÃO
print("Olá mundo!!!")

#INTRODUÇÃO COM VARIÁVEIS
nome = "Arthur"

print(nome)

#INTRODUÇÃO COM INPUT
nome = input("Digite o seu nome: ")

print(nome)

#INTRODUÇÃO COM INPUT E OUTPUT
print("=" * 50)
print("Seja bem vindo ao meu sistema! 😁")
print("=" * 50)

#DECLARAÇÕES DE VARIÁVEIS E ENTRADAS
nome = input("Insira o seu nome: ") #INPUT - RECEBE O NOME DO USUÁRIO
#email = input("Insira o seu mail: ") #INPUT - ARMAZENAR EMAIL DO USUÁRIO
#pais = input("Insira o país em que você reside: ") #INPUT - ARMAZENAR PAÍS DO USUÁRIO
#estado = input("Insira o estado que você mora: ") #INPUT - ARMAZENAR ESTADO DO USUÁRIO
#cidade = input("Insira a cidade que você mora: ") #INPUT - ARMAZENAR CIDADE DO USUÁRIO
#idadeAtual = int(input("Digite a sua idade: ")) #INPUT - ARMAZENAR A IDADE DO USUÁRIO EM INTEIRO
#idadeFutura = idadeAtual + 1
anoNascimento = int(input("Insira o ano que você nasceu:"))
anoAtual = int(input("Insira o ano que estamos: "))

#OUTPUT DAS INFORMAÇÕES INSERIDAS
#F ANTES DAS ASPAS SERVE PARA TRABALHAR COM VARIÁVEIS NO MEIO DA FRASE, {} SERVEM PARA INSERIR AS VARIÁVEIS.
#print(f"\nOlá, {nome}! Do país {pais}, morador da cidade de {cidade}, localizado no estado de {estado}. A sua idade é: {idadeAtual}. Estaremos enviando mísseis teleguiados para o e-mail: {email}. ")
#print(f"{nome}, no ano que vem, você terá: {idadeFutura} anos.")
print(f"\nOlá, {nome}, você tem {anoAtual - anoNascimento} anos!")