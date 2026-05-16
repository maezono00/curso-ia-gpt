import requests

print("-" * 50)
print("SISTEMA DE COMPRAS 3000 🛒")
print("-" * 50)

#recebe o cep digitado pelo usuário.
nome = input("Insira o seu nome: ")
email = input(f"{nome}, insira o seu e-mail: ")
telefone = input("Insira um telefone para contato: ")
cep = input("Por favor, insira seu CEP: ")

#url é uma variável que vai concatenar o link + a variável que recebeu o cep do usuário
url = (f"https://viacep.com.br/ws/{cep}/json/")

dados = requests.get(url).json()

print(f"Seja bem-vindo ao SISTEMA DE COMPRAS 2000, {nome}!!!\nO seu e-mail é: {email}\nO seu telefone é: {telefone}\nVocê mora na rua {dados['logradouro']}, na cidade de {dados['localidade']} e no estado de {dados['estado']}.")

# #O [], depois da variável que puxa as informações do request.get, serve para filtrar dados específicos.
# #atribuindo variáveis para cada um dos resultados.
# rua = dados['logradouro']
# cidade = dados['localidade']

# print(rua)
# print(cidade)