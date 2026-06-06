import requests as rq

cep = input("Digite o CEP da sua casa: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

dados = rq.get(url)

#TRATATIVA DO QUE FOI ARMAZENADO EM DADOS PARA JSON
resposta = dados.json()

# print(resposta)

#TRATATIVA DOS DADOS ONDE AS INFORMAÇÕES NECESSÁRIAS SERÃO ATRIBUÍDAS EM VARIÁVEIS
rua = resposta['logradouro']
bairro = resposta['bairro']
cidade = resposta['localidade']
estado = resposta['estado']

#IMPRESSÃO INTERATIVA USANDO OS DADOS DIRETAMENTE DO JSON
print(f"O usuário mora na rua {resposta["logradouro"]}, no bairro {resposta["bairro"]}, na cidade {resposta["localidade"]} e no estado de {resposta["estado"]}.")