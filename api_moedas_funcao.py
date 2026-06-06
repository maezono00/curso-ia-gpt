import requests

#PARA CRIAR FUNÇÃO, USAR COMANDO DEF
def get_moedas():
    url = "https://api.exchangerate-api.com/v4/latest/BRL"
    try:
        dados = requests.get(url)
        resposta = dados.json()
        
        valor_moeda_base = resposta['rates']['BRL']
        dolar = 1 / resposta['rates']['USD']
        euro = 1 / resposta['rates']['EUR']
    
        return f"{dolar:.2f} USD = 1 BRL | {euro:.2f} EUR = 1 BRL"
    except:
        return("Não foi possível realizar a conversão de valores.")
    
print(get_moedas())