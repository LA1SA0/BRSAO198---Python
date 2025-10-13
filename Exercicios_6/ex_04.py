'''4 - Crie um programa que realize consultas a  em relação ao Real (BRL) usando a API mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.'''

import requests

def consulta_moeda(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    try:
        response = requests.get(url)
        response.raise_for_status() 
        dados = response.json()
        
        chave = f"{moeda}BRL"
        if chave in dados:
            info = dados[chave]
            valor_atual = info['bid']
            valor_maximo = info['high']
            valor_minimo = info['low']
            ultima_atualizacao = info['create_date']
            
            print(f"Moeda: {moeda}/BRL")
            print(f"Valor Atual: R$ {valor_atual}")
            print(f"Valor Máximo: R$ {valor_maximo}")
            print(f"Valor Mínimo: R$ {valor_minimo}")
            print(f"Última Atualização: {ultima_atualizacao}")
        else:
            print("Moeda não encontrada.")
    except requests.exceptions.RequestException as e:
        print("Erro na requisição:", e)

moeda = input("Digite a sigla da moeda (ex: USD, EUR, GBP): ").upper()
consulta_moeda(moeda)

