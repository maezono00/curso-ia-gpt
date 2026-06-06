import requests

#BIBLIOTECA DE SISTEMA
import os

# api_key = os.getenv("OPENWEATHER_API_KEY")
api_key = "" #INSIRA CHAVE

cidade = "Americana"

url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt"

dados = requests.get(url)
resposta = dados.json()

temperaturaAtual = resposta['main']['temp']
umidade = resposta['main']['humidity']

descricao = resposta['weather'][0]['description']

print(temperaturaAtual)
print(umidade)
print(descricao)