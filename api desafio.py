import requests

#recebe o cep digitado pelo usuário.
cep = input("Por favor, insira seu CEP: ")

#url é uma variável que vai concatenar o link + a variável que recebeu o cep do usuário
url = (f"https://viacep.com.br/ws/{cep}/json/")

dados = requests.get(url).json()

#O [], depois da variável que puxa as informações do request.get, serve para filtrar dados específicos.
#atribuindo variáveis para cada um dos resultados.
rua = dados['logradouro']
cidade = dados['localidade']

print(rua)
print(cidade)