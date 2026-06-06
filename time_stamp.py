#CONVERSÃO DE TIMESTAMP PARA UM FORMATO DE HORAS LEGÍVEL
from datetime import datetime

time_stamp = 1780704002
data_atualizada = datetime.fromtimestamp(time_stamp)

print(data_atualizada)