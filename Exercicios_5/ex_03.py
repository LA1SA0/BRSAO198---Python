'''3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.
'''

def calcular_desconto(preco, percentual):
    return preco * (percentual / 100)

def preco_final(preco, percentual):
    desconto = calcular_desconto(preco, percentual)
    return round(preco - desconto, 2)

try:
    preco = float(input("Digite o preço do produto: R$ "))
    percentual = float(input("Digite o percentual de desconto: "))
    
    if preco < 0 or percentual < 0:
        print("Preço e percentual devem ser valores positivos.")
    else:
        novo_preco = preco_final(preco, percentual)
        print(f"O preço final após {percentual}% de desconto é: R$ {novo_preco:.2f}")
except ValueError:
    print("Por favor, insira valores numéricos válidos.")
