#INSTALAR BIBLIOTECAS
#pip install requests

#ADICIONAR/IMPORTAR BIBLIOTECA NO CÓDIGO
import requests

url = "https://viacep.com.br/ws/13083-760/json/"

#.get é de visualizar
dados = requests.get(url).json()

print(dados)
