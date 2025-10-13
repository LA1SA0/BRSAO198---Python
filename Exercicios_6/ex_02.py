'''2 -   Crie um programa que  acesse a API  para buscar um usuário fictício aleatório. exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.'''

import requests
from requests.exceptions import RequestException

url = 'https://randomuser.me/api/'

try:
    response = requests.get(url)
    response.raise_for_status()  
    data = response.json()  

    user = data['results'][0]
    name = f"{user['name']['first']} {user['name']['last']}"
    email = user['email']
    country = user['location']['country']

    print(f"Nome: {name}")
    print(f"E-mail: {email}")
    print(f"País: {country}")

except RequestException as e:
    print(f"Falha na conexão: {e}")