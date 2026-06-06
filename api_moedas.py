#API QUE CONVERTE MOEDAS
import requests

#URL DA API
url = f"https://api.exchangerate-api.com/v4/latest/BRL"

dados = requests.get(url)
resposta = dados.json()

#CHAMAR UM DICIONÁRIO QUE ESTÁ DENTRO DE OUTRO DICIONÁRIO
# moedaBase = resposta['rates']['BRL']

# print(moedaBase)
valor_moeda_base = resposta['rates']['BRL']
dolar = 1 / resposta['rates']['USD']
euro = 1 / resposta['rates']['EUR']

print(f"{dolar:.2f} BRL = 1 USD")
print(f"{euro:.2f} BRL = 1 EURO")