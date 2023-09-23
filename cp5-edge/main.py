import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime

# Fazer a solicitação HTTP
url = "http://46.17.108.113:8666/STH/v1/contextEntities/type/Lamp/id/urn:ngsi-ld:Lamp:050/attributes/luminosity?lastN=100"
headers = {
    'fiware-service': 'smart',
    'fiware-servicepath': '/'
}
response = requests.get(url, headers=headers)

# Analisar os dados JSON
data = json.loads(response.text)
values = data['contextResponses'][0]['contextElement']['attributes'][0]['values']

# Extrair timestamps e valores de luminosidade
timestamps = [datetime.strptime(value['recvTime'], "%Y-%m-%dT%H:%M:%S.%fZ") for value in values]
luminosity_values = [value['attrValue'] for value in values]

# Criar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(timestamps, luminosity_values, marker='o', linestyle='-', color='b')
plt.title('Luminosidade ao longo do tempo')
plt.xlabel('Tempo')
plt.ylabel('Luminosidade')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar o gráfico
plt.show()