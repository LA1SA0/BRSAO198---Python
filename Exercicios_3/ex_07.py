'''7 - Crie um programa que percorre uma lista de números inteiros e imprime apenas os que são números primos. Use o for para iterar, if para a verificação e continue para pular os que não são primos.'''
def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
numeros = [10, 15, 23, 42, 7, 3, 8, 19, 25, 29]
for numero in numeros:
    if not eh_primo(numero):
        continue
    print(f"{numero} é um número primo.")
