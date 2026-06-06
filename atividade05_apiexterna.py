import requests

def getMoedas():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    try:
        dados = requests.get(url)
        resposta = dados.json()
        
        # moedaBase = resposta['rates']['USD']
        
        moedaReal = resposta['rates']['BRL']
        moedaEuro = resposta['rates']['EUR']
        moedaLibraE = resposta['rates']['GBP']
        moedaPesoA = resposta['rates']['ARS']
        
        return(f"{moedaReal:.2f} BRL = 1 USD | {moedaEuro:.2f} EUR = 1 USD | {moedaLibraE:.2f} GBP = 1 USD | {moedaPesoA:.2f} ARS = 1 USD.")
    except:
        return("Não foi possível fazer a conversão, tente novamente mais tarde.")
        
print(getMoedas())